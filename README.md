# Simple File Upload Server

A simple Flask web application that allows you to upload files and folders through a web interface.

🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡🚀⚡

# TL;DR

## Quick Start:
```bash
pip install -r requirements.txt
python app.py
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
- **API Upload**: Supports programmatic uploads via `/uppy_upload` endpoint

### File Management
- **Preview**: See thumbnails for images and videos, text previews for text files
- **Download**: Download any uploaded file with secure filename handling
- **File List**: View all uploaded files sorted by modification time (newest first)
- **File Information**: Displays file types and basic metadata

### Security Features
- **File Type Validation**: Only allows predefined file types (see allowed extensions list)
- **Path Protection**: Prevents directory traversal attacks
- **Secure Filenames**: Sanitizes file names to prevent issues
- **File Size Limits**: Maximum 1GB per file (with smart warnings for larger files)
- **Dynamic Limits**: Temporary size limit increases with user consent for large files

### Allowed File Types
- **Images**: png, jpg, jpeg, gif
- **Videos**: mp4, avi, mov, mkv, webm, flv, wmv
- **Documents**: txt, pdf, doc, docx
- **Archives**: zip, rar, 7z, tar, gz
- **Applications**: apk, exe, msi, dmg, iso, bin, app, deb, rpm
- **Scripts**: bat, sh

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
✅ File type validation (allows safe file types - see allowed extensions list)  
✅ Path traversal protection (can't access system files)  
✅ Secure filename handling  
✅ File size limits  
✅ Input sanitization  

### What to Be Aware Of:
⚠️ This is designed for **local network use**  
⚠️ Don't expose to the internet without additional security  
⚠️ Anyone on your network can access uploaded files  
⚠️ Some executable file types are allowed - be cautious with files from untrusted sources  

---

## API Endpoints

For programmatic access, the server provides these endpoints:

### Upload Endpoints
- `POST /` - Main upload form (handles multiple files)
- `POST /upload_folder` - Folder upload with structure preservation
- `POST /uppy_upload` - Single file upload API (returns simple OK/error response)

### File Access
- `GET /uploads/<filename>` - Direct file access (for previews and downloads)
- `GET /download/<filename>` - Force download with attachment headers

### Usage Example:
```bash
# Upload a single file via API
curl -X POST -F "file=@example.txt" http://localhost:5000/uppy_upload
```

---

## Configuration

### Environment Variables:
```bash
# Set a custom secret key (recommended for production)
export SECRET_KEY="your-very-long-random-string-here"
```

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
