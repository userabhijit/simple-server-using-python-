from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os
from werkzeug.utils import secure_filename
import socket
from mimetypes import guess_type

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 * 1024  # 1GB max file size
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions for security
ALLOWED_EXTENSIONS = {
    'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif',
    'mp4', 'avi', 'mov', 'mkv', 'webm', 'flv', 'wmv',
    'doc', 'docx', 'zip', 'rar', '7z', 'tar', 'gz',
    'apk', 'exe', 'msi', 'dmg', 'iso', 'bin', 'app', 'deb', 'rpm', 'bat', 'sh', 'cmd',
    'msu', 'cab', 'ps1', 'scr', 'cpl', 'vbs', 'jar', 'com', 'msc', 'lnk'
}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def secure_path(filename):
    """Secure the file path to prevent directory traversal attacks"""
    # Remove any path traversal attempts
    filename = filename.replace('..', '').replace('\\', '/').strip('/')
    # Use secure_filename for additional security
    parts = filename.split('/')
    secured_parts = [secure_filename(part) for part in parts if part]
    return '/'.join(secured_parts)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_file_preview(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    mime, _ = guess_type(filepath)
    if mime and mime.startswith('image/'):
        return {'type': 'image', 'src': url_for('uploaded_file', filename=filename)}
    elif mime and mime.startswith('video/'):
        return {'type': 'video', 'src': url_for('uploaded_file', filename=filename)}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = [f.readline() for _ in range(5)]
        return {'type': 'text', 'content': ''.join(lines)}
    except Exception:
        return {'type': 'none'}

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('file')
        if not files or all(f.filename == '' for f in files):
            flash('No selected file')
            return redirect(request.url)
        for file in files:
            if file and file.filename != '':
                if not allowed_file(file.filename):
                    flash(f'File type not allowed for "{file.filename}"')
                    continue
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash(f'File "{filename}" uploaded successfully!')
        return redirect(url_for('index'))
    # Sort files by modification time, latest first
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    files = sorted(files, key=lambda f: os.path.getmtime(os.path.join(app.config['UPLOAD_FOLDER'], f)), reverse=True)
    previews = {f: get_file_preview(f) for f in files}
    local_ip = get_local_ip()
    server_url = f"http://{local_ip}:5000/"
    allowed_exts = sorted(ALLOWED_EXTENSIONS)
    return render_template('index.html', files=files, previews=previews, local_ip=local_ip, server_url=server_url, allowed_exts=allowed_exts)

@app.route('/download/<filename>')
def download_file(filename):
    # Secure the filename to prevent directory traversal
    filename = secure_filename(filename)
    # Check if file exists in upload folder
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(file_path) or not os.path.commonpath([app.config['UPLOAD_FOLDER'], file_path]) == app.config['UPLOAD_FOLDER']:
        flash('File not found')
        return redirect(url_for('index'))
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/upload_folder', methods=['POST'])
def upload_folder():
    # Check for temporary size limit increase
    temp_max_size = request.form.get('tempMaxSize')
    original_limit = app.config['MAX_CONTENT_LENGTH']
    
    if temp_max_size:
        try:
            temp_limit = int(temp_max_size)
            # Temporarily increase the limit
            app.config['MAX_CONTENT_LENGTH'] = temp_limit
            print(f"Temporarily increased upload limit to {temp_limit / (1024*1024*1024):.2f} GB")
        except (ValueError, TypeError):
            print("Invalid temporary size limit, using default")
    
    try:
        files = request.files.getlist('files')
        uploaded = 0
        failed = 0
        for file in files:
            if file and file.filename:
                if not allowed_file(file.filename):
                    failed += 1
                    continue
                rel_path = secure_path(file.filename)
                if not rel_path:  # Skip if path becomes empty after sanitization
                    failed += 1
                    continue
                save_path = os.path.join(app.config['UPLOAD_FOLDER'], rel_path)
                try:
                    os.makedirs(os.path.dirname(save_path), exist_ok=True)
                    file.save(save_path)
                    uploaded += 1
                except Exception as e:
                    failed += 1
                    print(f"Error saving file {rel_path}: {e}")
        
        if uploaded > 0:
            flash(f'{uploaded} file(s) uploaded successfully!')
        if failed > 0:
            flash(f'{failed} file(s) failed to upload (invalid type or path)')
            
    finally:
        # Always restore the original limit
        app.config['MAX_CONTENT_LENGTH'] = original_limit
        if temp_max_size:
            print(f"Restored upload limit to {original_limit / (1024*1024*1024):.2f} GB")
    
    return redirect(url_for('index'))

@app.route('/uppy_upload', methods=['POST'])
def uppy_upload():
    if 'file' not in request.files:
        return 'No file provided', 400
    
    file = request.files['file']
    if not file.filename:
        return 'No filename provided', 400
        
    if not allowed_file(file.filename):
        return 'File type not allowed', 400
        
    rel_path = secure_path(file.filename)
    if not rel_path:
        return 'Invalid file path', 400
        
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], rel_path)
    try:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        file.save(save_path)
        return 'OK'
    except Exception as e:
        print(f"Error saving file {rel_path}: {e}")
        return 'Upload failed', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False ) 