# YouTube Downloader User Guide

## Program Overview
This program is a GUI application that allows you to download videos or audio (music) from YouTube.

## Key Features
- ✓ Download YouTube videos (highest quality)
- ✓ Download audio only as MP3
- ✓ Freely choose download location
- ✓ Intuitive GUI interface
- ✓ Real-time download progress display

## How to Run

### Method 1: Run EXE File (Recommended)
```
dist\YouTube_Downloader.exe
```
- Simply double-click the `dist\YouTube_Downloader.exe` file in Windows Explorer.
- No additional installation or configuration required.

### Method 2: Run Directly with Python
```
python youtube_downloader.py
```

## Usage Instructions

1. **Enter YouTube URL**
   - Paste the URL of the YouTube video you want to download in the "YouTube URL" input box.
   - Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ

2. **Set Save Location**
   - Enter your desired save location in the "Save Location" input box.
   - Click the "Browse" button to select a folder.
   - Default: `C:\Users\[Username]\Downloads\YouTube`

3. **Select Download Option**
   - **Download Video**: Downloads the original video file (recommended quality)
   - **Download Audio Only (MP3)**: Downloads only the audio track as MP3 format.

4. **Start Download**
   - Click the "Download" button.
   - Progress will be displayed in the log window at the bottom.
   - When download is complete, a "Download Complete!" message will appear.

5. **Reset Path** (Optional)
   - Click the "Reset Path" button to reset the save location to default.

## System Requirements

### For Running EXE File
- Windows 7 or later
- Internet connection
- At least 100MB free disk space (actual space depends on downloaded files)

### For Running with Python
- Python 3.8 or later
- Install the following packages:
  ```
  pip install yt-dlp PySimpleGUI ffmpeg-python
  ```

## Troubleshooting

### 1. "FFmpeg not found" Error
- FFmpeg is not installed.
- Run the following command in Windows Command Prompt:
  ```
  pip install ffmpeg-python
  ```
  Or install directly from https://ffmpeg.org/download.html

### 2. "Network Error"
- Check your internet connection.
- Verify YouTube server status.
- Verify the URL is correct.

### 3. "Save Path Error"
- Verify the path you entered exists.
- Ensure the path contains no special characters.
- Check available disk space.

### 4. Audio Download Not in MP3 Format
- FFmpeg may not be installed correctly.
- Refer to the "FFmpeg not found" solution above.

## File Structure

```
Workspace/
├── youtube_downloader.py          # Main program source code
├── build.bat                      # Build script (Windows batch file)
├── YouTube_Downloader.spec        # PyInstaller spec file
├── dist/
│   └── YouTube_Downloader.exe     # Final executable file
├── build/                          # Temporary files created during build
├── README.md                       # Korean version documentation
└── README_EN.md                    # English version documentation
```

## Technical Information

- **Language**: Python 3.14
- **GUI Library**: PySimpleGUI
- **Download Library**: yt-dlp
- **Audio Conversion**: ffmpeg
- **Build Tool**: PyInstaller

## Important Notes

1. **Copyright**: The copyright of content downloaded from YouTube belongs to the original creator.
   Do not distribute without permission except for personal use.

2. **YouTube Terms of Service**: You must comply with YouTube's Terms of Service.

3. **Antivirus Warning**: The EXE file may be flagged by antivirus programs.
   This is a common false positive caused by PyInstaller.

## License

This project is free to use for personal purposes.

## Support

If you encounter any issues, please check:
1. Internet connection status
2. Validity of the YouTube URL
3. Validity of the save path
4. Available disk space
