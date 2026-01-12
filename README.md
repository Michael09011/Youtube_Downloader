# YouTube 다운로더 사용 설명서

## 프로그램 개요
이 프로그램은 YouTube에서 동영상 또는 음성(음악)을 다운로드할 수 있는 GUI 애플리케이션입니다.

## 주요 기능
- ✓ YouTube 동영상 다운로드 (최고 화질)
- ✓ YouTube 음성만 MP3로 다운로드
- ✓ 저장 경로 자유롭게 선택 가능
- ✓ 직관적인 GUI 인터페이스
- ✓ 다운로드 진행 상황 실시간 표시

## 실행 방법

### 방법 1: EXE 파일로 실행 (권장)
```
dist\YouTube_Downloader.exe
```
- Windows 탐색기에서 `dist\YouTube_Downloader.exe` 파일을 더블클릭하면 됩니다.
- 추가 설치나 설정이 필요 없습니다.

### 방법 2: Python으로 직접 실행
```
python youtube_downloader.py
```

## 사용 방법

1. **YouTube URL 입력**
   - "YouTube URL" 입력 상자에 다운로드하려는 YouTube 동영상의 URL을 붙여넣습니다.
   - 예: https://www.youtube.com/watch?v=dQw4w9WgXcQ

2. **저장 경로 설정**
   - "저장 경로" 입력 상자에 원하는 저장 위치를 입력합니다.
   - "찾아보기" 버튼을 클릭하여 폴더를 선택할 수 있습니다.
   - 기본값: `C:\Users\[사용자명]\Downloads\YouTube`

3. **다운로드 옵션 선택**
   - **동영상 다운로드**: 원본 동영상 파일을 다운로드합니다 (권장 화질)
   - **음성만 다운로드 (MP3)**: 음성 트랙만 MP3 형식으로 다운로드합니다.

4. **다운로드 시작**
   - "다운로드" 버튼을 클릭합니다.
   - 진행 상황이 하단의 로그 창에 표시됩니다.
   - 다운로드가 완료되면 "다운로드 완료!" 메시지가 표시됩니다.

5. **경로 초기화** (선택사항)
   - "경로 초기화" 버튼을 클릭하면 저장 경로가 기본값으로 리셋됩니다.

## 필수 요구사항

### EXE 파일 실행
- Windows 7 이상
- 인터넷 연결
- 최소 100MB의 여유 디스크 공간 (용량은 다운로드 파일에 따라 다름)

### Python으로 실행하려는 경우
- Python 3.8 이상
- 다음 패키지 설치 필요:
  ```
  pip install yt-dlp PySimpleGUI ffmpeg-python
  ```

## 문제 해결

### 1. "FFmpeg not found" 오류
- FFmpeg가 설치되지 않았습니다.
- Windows 명령 프롬프트에서 다음을 실행하세요:
  ```
  pip install ffmpeg-python
  ```
  또는 https://ffmpeg.org/download.html 에서 직접 설치합니다.

### 2. "네트워크 오류"
- 인터넷 연결을 확인하세요.
- YouTube 서버 상태를 확인하세요.
- URL이 올바른지 확인하세요.

### 3. "저장 경로 오류"
- 입력한 경로가 존재하는지 확인하세요.
- 경로에 특수문자가 없는지 확인하세요.
- 디스크 여유 공간을 확인하세요.

### 4. 음성 다운로드가 MP3가 아님
- FFmpeg가 올바르게 설치되지 않았을 수 있습니다.
- 위의 "FFmpeg not found" 해결 방법을 참고하세요.

## 파일 구조

```
Workspace/
├── youtube_downloader.py          # 메인 프로그램 소스 코드
├── build.bat                      # 빌드 스크립트 (Windows 배치 파일)
├── YouTube_Downloader.spec        # PyInstaller 스펙 파일
├── dist/
│   └── YouTube_Downloader.exe     # 최종 실행 파일
├── build/                          # 빌드 과정에서 생성되는 임시 파일
└── README.md                       # 이 파일
```

## 기술 정보

- **언어**: Python 3.14
- **GUI 라이브러리**: PySimpleGUI
- **다운로드 라이브러리**: yt-dlp
- **음성 변환**: ffmpeg
- **빌드 도구**: PyInstaller

## 주의사항

1. **저작권**: YouTube에서 다운로드한 콘텐츠의 저작권은 원래 제작자에게 있습니다.
   개인 사용 목적 외에는 허가 없이 배포하면 안 됩니다.

2. **YouTube 약관**: YouTube의 서비스 약관을 준수해야 합니다.

3. **바이러스 검사**: EXE 파일이 안티바이러스 프로그램에 의해 경고될 수 있습니다.
   이는 PyInstaller에 의해 일반적으로 발생하는 오탐지입니다.

## 라이선스

이 프로젝트는 개인 사용 목적으로 자유롭게 사용할 수 있습니다.

## 지원

문제가 발생하면 다음을 확인하세요:
1. 인터넷 연결 상태
2. YouTube URL의 유효성
3. 저장 경로의 유효성
4. 디스크 여유 공간
