@echo off
REM YouTube 다운로더를 EXE로 빌드하는 스크립트
REM 사전에 pyinstaller를 설치해야 합니다: pip install pyinstaller

echo YouTube 다운로더를 EXE 파일로 빌드 중입니다...
echo.

REM PyInstaller를 사용하여 EXE 파일 생성
pyinstaller --onefile ^
    --windowed ^
    --name "YouTube_Downloader" ^
    --add-data "ffmpeg-python:ffmpeg_python" ^
    youtube_downloader.py

echo.
echo 빌드 완료! dist\YouTube_Downloader.exe 파일을 확인하세요.
pause
