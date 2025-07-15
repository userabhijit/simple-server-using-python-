# Simple File Upload Server

A simple Flask web application that allows you to upload files and folders through a web interface.

🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡

# TL;DR

## Quick Start:
```bash
pip install -r requirements.txt
python app.py
```

## ⚠️ Security First (Optional for Local Network):
```bash
# For local network use, the app will work without setting a SECRET_KEY
# (Flask will generate one automatically)
python app.py

# BUT, if you want consistent sessions across server restarts:
# Windows PowerShell:
$env:SECRET_KEY="any-random-string-you-want"

# Linux/Mac:
export SECRET_KEY="any-random-string-you-want"
```

## Then open the URL shown in your browser (usually `http://your-ip:5000`) and start uploading files!

## What it does: 
### Web-based file upload server that works on your local network. Upload files/folders from any device, preview them, and download them later.

🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡
## What This Does

This is a **file upload server** that:
- 📁 Upload individual files or entire folders
- 🌐 Access from any device on your network
- 👀 Preview images, videos, and text files
- ⬇️ Download uploaded files
- 📱 Works on mobile and desktop

## How It Works

### Simple Explanation:
1. **Start the server** - Run the Python script
2. **Open your browser** - Go to the displayed URL
3. **Upload files** - Click "Choose Files" and select what you want to upload
4. **Access anywhere** - Other devices on your network can also access the URL

### Technical Details:
- **Flask** - Python web framework that handles requests
- **Werkzeug** - Provides security utilities (like safe file names)
- **HTML/CSS/JavaScript** - Creates the web interface
- **File Storage** - Files are saved to the `uploads/` folder

---

## Project Structure

```
simple-server/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies  
├── README.md          # This file
├── .gitignore         # Git ignore rules (excludes uploads/, .env, etc.)
├── .env.example       # Template for environment variables
├── static/
│   └── styles.css     # CSS styling for the web interface
├── templates/
│   └── index.html     # Main HTML template
└── uploads/           # Directory for uploaded files (auto-created, git-ignored)
```

---

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

**What gets installed:**
- `Flask==2.3.3` - The web framework
- `Werkzeug==2.3.7` - Security and utility functions

### Step 2: Run the Server
```bash
# Start the server
python app.py
```

### Step 3: Access the Web Interface
1. Look for output like: `Running on http://192.168.1.100:5000/`
2. Open that URL in your browser
3. Start uploading files!

---

## Project Structure

```
simple server(using python)/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── templates/
│   └── index.html     # Web interface
├── static/
│   └── styles.css     # Styling
└── uploads/           # Where files are stored (created automatically)
```

---

## Features

### File Upload
- **Single Files**: Choose individual files to upload
- **Folders**: Upload entire folder structures (preserves folder organization)
- **Multiple Files**: Select multiple files at once
- **Progress Tracking**: See upload progress for each file
- **Smart Size Limits**: Automatically detects large files (>1GB) and warns user about potential issues
- **Temporary Limit Increase**: Allows temporary size limit increases for large files with user consent

### File Management
- **Preview**: See thumbnails for images and videos
- **Download**: Download any uploaded file
- **File List**: View all uploaded files in a table

### Security Features
- **File Type Validation**: Only allows safe file types
- **Path Protection**: Prevents directory traversal attacks
- **Secure Filenames**: Sanitizes file names to prevent issues
- **File Size Limits**: Maximum 1GB per file (with smart warnings for larger files)
- **Dynamic Limits**: Temporary size limit increases with user consent for large files

### Allowed File Types
- **Images**: png, jpg, jpeg, gif
- **Videos**: mp4, avi, mov, mkv
- **Documents**: txt, pdf, doc, docx
- **Archives**: zip, rar

---

## How to Use

### Basic Upload:
1. Click the file input area
2. Select files or folders
3. **Large File Warning**: If files >1GB are detected, you'll see a warning with:
   - Upload time estimate
   - Memory requirements
   - Potential issues (timeouts, network problems)
   - Option to proceed or choose smaller files
4. Click "Upload Folder" button
5. Wait for upload to complete

### Large File Handling:
When you select files larger than 1GB, the system will:
- **Warn you** about potential issues (long upload times, memory usage, timeouts)
- **Estimate upload time** based on typical connection speeds
- **Ask for confirmation** before proceeding
- **Temporarily increase** the upload limit if you choose to continue
- **Automatically restore** the 1GB limit after upload completes

### Access from Other Devices:
1. Make sure devices are on the same network
2. Use the Server URL shown on the page
3. Enter that URL in any browser

### Download Files:
1. Scroll down to "Available Files" section
2. Click "Download" next to any file

---

## Troubleshooting

### Common Issues:

**"Can't access from other devices"**
- Make sure all devices are on the same WiFi network
- Check if firewall is blocking port 5000

**"Upload failed"**
- Check if file type is allowed
- Make sure file is under 1GB
- Check available disk space

**"Permission denied"**
- Make sure you have write permissions in the project folder
- Try running as administrator (Windows) or with sudo (Mac/Linux)

**"Uploads folder issues"**
- The `uploads/` folder is automatically created when first needed
- This folder is excluded from git (contains user data, not source code)
- If you need to reset: stop the server, delete `uploads/` folder, restart

### Technical Issues:

**Import errors:**
```bash
# Make sure dependencies are installed
pip install Flask Werkzeug
```

**Port already in use:**
- Close other applications using port 5000
- Or change the port in app.py: `app.run(host='0.0.0.0', port=5001)`

---

## Security Notes

### What's Protected:
✅ File type validation (no executable files)  
✅ Path traversal protection (can't access system files)  
✅ Secure filename handling  
✅ File size limits (1GB default)  
✅ Input sanitization  
✅ Directory traversal prevention  

### What to Be Aware Of:
⚠️ **Local Network Only**: This is designed for local network use  
⚠️ **No Authentication**: Anyone on your network can upload/download files  
⚠️ **Internet Exposure**: Never expose directly to the internet without authentication  
⚠️ **Disk Space**: Uploaded files are stored locally - monitor available space  

### When You Need a SECRET_KEY:
- **Internet Deployment**: If exposing beyond your local network
- **Session Persistence**: If you want upload status messages to persist across server restarts
- **Production Use**: For any production or shared environment
- **Authentication**: If you plan to add user login features later  

### Security Recommendations:
- **Always set a custom SECRET_KEY** using environment variables
- **Never commit sensitive files** to version control (uploads/, .env files)
- **Use HTTPS** for secure connections
- **Implement authentication** for production environments
- **Regular security updates** - keep Flask and dependencies updated
- **Monitor uploads folder** for suspicious files
- **Backup uploaded files** regularly

---

## Configuration

### Environment Variables:

**For Local Network Use:**
```bash
# No setup required! Just run:
python app.py
```

**For Consistent Sessions (Optional):**
```bash
# Option 1: Simple environment variable
# Windows PowerShell:
$env:SECRET_KEY="my-local-server-key"

# Linux/Mac:
export SECRET_KEY="my-local-server-key"
```

**For Production/Internet Use:**
```bash
# Option 1: Using .env file (Recommended)
cp .env.example .env
# Edit .env and set a strong SECRET_KEY

# Option 2: Strong random key
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_hex(32))')"
```

### Important Files (Git Management):
- ✅ **Included in Git**: Source code, templates, static files, requirements.txt
- ❌ **Excluded from Git**: uploads/, .env files, logs/, __pycache__/
- 📁 **`.gitignore` file** automatically excludes sensitive files and folders

### Customization:
- **Change upload folder**: Edit `UPLOAD_FOLDER` in `app.py`
- **Add file types**: Edit `ALLOWED_EXTENSIONS` in `app.py`
- **Change file size limit**: Edit `MAX_CONTENT_LENGTH` in `app.py`
- **Change port**: Edit the `app.run()` line in `app.py`

---

## Development

### Adding New Features:
1. **Backend**: Modify `app.py` for new routes or functionality
2. **Frontend**: Edit `templates/index.html` for UI changes
3. **Styling**: Update `static/styles.css` for appearance changes

### Testing:
```bash
# Run in debug mode for development
# Change debug=False to debug=True in app.py
```

---

## License

This is a simple educational project. Feel free to modify and use as needed.

---

**Need Help?** Check the troubleshooting section above or review the code comments in `app.py`.
