import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import threading
from pathlib import Path
import subprocess
import sys

try:
    import yt_dlp
except ImportError:
    print("yt-dlp를 설치 중입니다...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp", "--upgrade"])
    import yt_dlp

# 기본 다운로드 경로
DEFAULT_DOWNLOAD_PATH = str(Path.home() / "Downloads" / "YouTube")

# 색상 팔레트
COLORS = {
    'bg': '#f0f2f5',
    'fg': '#1c1e21',
    'primary': '#0a66c2',
    'primary_hover': '#084a94',
    'success': '#31a24c',
    'danger': '#e74c3c',
    'warning': '#f39c12',
    'text_light': '#65676b',
}

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube 다운로더")
        self.root.geometry("800x650")
        self.root.resizable(True, True)
        self.root.configure(bg=COLORS['bg'])
        
        # 커스텀 스타일 설정
        self.setup_styles()
        
        # 메인 프레임
        main_frame = tk.Frame(root, bg=COLORS['bg'])
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=0, pady=0)
        
        # 헤더 섹션
        self.create_header(main_frame)
        
        # 입력 섹션
        self.create_input_section(main_frame)
        
        # 옵션 섹션
        self.create_options_section(main_frame)
        
        # 버튼 섹션
        self.create_button_section(main_frame)
        
        # 진행 상황 섹션
        self.create_progress_section(main_frame)
        
        # 로그 섹션
        self.create_log_section(main_frame)
        
        # 그리드 가중치 설정
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
    
    def setup_styles(self):
        """커스텀 스타일 설정"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # 메인 프레임 스타일
        style.configure('Main.TFrame', background=COLORS['bg'])
        
        # 헤더 스타일
        style.configure('Header.TFrame', background='#ffffff', relief='flat')
        
        # 섹션 레이블 스타일
        style.configure('Section.TLabel', background=COLORS['bg'], 
                       font=('Segoe UI', 11, 'bold'), foreground=COLORS['fg'])
        
        # 일반 레이블 스타일
        style.configure('TLabel', background=COLORS['bg'], foreground=COLORS['fg'],
                       font=('Segoe UI', 9))
        
        # 엔트리 스타일
        style.configure('TEntry', fieldbackground='#ffffff', font=('Segoe UI', 9))
        
        # 라디오버튼 스타일
        style.configure('TRadiobutton', background=COLORS['bg'], foreground=COLORS['fg'],
                       font=('Segoe UI', 9))
        
        # 체크버튼 스타일
        style.configure('TCheckbutton', background=COLORS['bg'], foreground=COLORS['fg'],
                       font=('Segoe UI', 9))
        
        # 버튼 스타일
        style.configure('Primary.TButton', font=('Segoe UI', 10, 'bold'))
        style.configure('Secondary.TButton', font=('Segoe UI', 10))
        style.map('Primary.TButton',
                 background=[('active', COLORS['primary_hover'])],
                 foreground=[('active', '#ffffff')])
    
    def create_header(self, parent):
        """헤더 섹션 생성"""
        header = tk.Frame(parent, bg='#ffffff', height=60)
        header.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=0, pady=0)
        header.grid_propagate(False)
        
        title = tk.Label(header, text="YouTube 다운로더", 
                         font=('Segoe UI', 18, 'bold'),
                         bg='#ffffff', fg=COLORS['primary'])
        title.grid(row=0, column=0, sticky=tk.W, padx=20, pady=15)
        
        subtitle = tk.Label(header, text="동영상 또는 음성을 손쉽게 다운로드하세요",
                            font=('Segoe UI', 9), bg='#ffffff',
                            fg=COLORS['text_light'])
        subtitle.grid(row=1, column=0, sticky=tk.W, padx=20, pady=(0, 5))
        
        # 구분선
        separator = tk.Frame(header, bg='#e5e7eb', height=1)
        separator.grid(row=2, column=0, sticky=(tk.W, tk.E), padx=0, pady=0)
    
    def create_input_section(self, parent):
        """입력 섹션 생성"""
        section = tk.Frame(parent, bg=COLORS['bg'])
        section.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=20, pady=15)
        section.columnconfigure(1, weight=1)
        
        # URL 레이블
        ttk.Label(section, text="YouTube URL:", style='Section.TLabel').grid(
            row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        # URL 입력 필드
        self.url_entry = ttk.Entry(section, width=60)
        self.url_entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # 저장 경로 레이블
        ttk.Label(section, text="저장 경로:", style='Section.TLabel').grid(
            row=2, column=0, sticky=tk.W, pady=(0, 5))
        
        # 저장 경로 프레임
        path_frame = ttk.Frame(section)
        path_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))
        path_frame.columnconfigure(0, weight=1)
        
        self.path_entry = ttk.Entry(path_frame, width=45)
        self.path_entry.insert(0, DEFAULT_DOWNLOAD_PATH)
        self.path_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        browse_btn = ttk.Button(path_frame, text="찾아보기", command=self.browse_folder,
                               style='Secondary.TButton')
        browse_btn.grid(row=0, column=1, padx=(10, 0))
    
    def create_options_section(self, parent):
        """옵션 섹션 생성"""
        section = tk.Frame(parent, bg=COLORS['bg'])
        section.grid(row=2, column=0, sticky=(tk.W, tk.E), padx=20, pady=10)
        section.columnconfigure(0, weight=1)
        
        ttk.Label(section, text="다운로드 옵션:", style='Section.TLabel').grid(
            row=0, column=0, sticky=tk.W, pady=(0, 10))
        
        # 다운로드 타입 선택
        options_frame = tk.Frame(section, bg=COLORS['bg'])
        options_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=(0, 0))
        
        self.download_type = tk.StringVar(value="video")
        ttk.Radiobutton(options_frame, text="📹 동영상 다운로드", 
                       variable=self.download_type, value="video").pack(anchor=tk.W, pady=3)
        ttk.Radiobutton(options_frame, text="🎵 음성만 다운로드 (MP3)", 
                       variable=self.download_type, value="audio").pack(anchor=tk.W, pady=3)
        
        # 자막 옵션
        subtitle_frame = tk.LabelFrame(section, text="자막 옵션", bg=COLORS['bg'],
                                       fg=COLORS['fg'], font=('Segoe UI', 10, 'bold'),
                                       padx=10, pady=10)
        subtitle_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
        self.subtitle_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(subtitle_frame, text="동영상에 자막 포함하기 (한국어, 영어 등)",
                       variable=self.subtitle_var).pack(anchor=tk.W)
        ttk.Label(subtitle_frame, text="💡 자막을 포함하면 다운로드 시간이 조금 더 걸릴 수 있습니다.",
                 font=('Segoe UI', 8), foreground=COLORS['text_light']).pack(anchor=tk.W, pady=(5, 0))
    
    def create_button_section(self, parent):
        """버튼 섹션 생성"""
        button_frame = tk.Frame(parent, bg=COLORS['bg'])
        button_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), padx=20, pady=15)
        button_frame.columnconfigure(1, weight=1)
        
        self.download_btn = ttk.Button(button_frame, text="다운로드 시작", 
                                      command=self.start_download, style='Primary.TButton')
        self.download_btn.grid(row=0, column=0, padx=(0, 10))
        
        reset_btn = ttk.Button(button_frame, text="초기화", command=self.reset_path,
                              style='Secondary.TButton')
        reset_btn.grid(row=0, column=1, sticky=tk.W, padx=5)
        
        exit_btn = ttk.Button(button_frame, text="종료", command=self.root.quit,
                             style='Secondary.TButton')
        exit_btn.grid(row=0, column=2, sticky=tk.W, padx=5)
    
    def create_progress_section(self, parent):
        """진행 상황 섹션 생성"""
        section = tk.Frame(parent, bg=COLORS['bg'])
        section.grid(row=4, column=0, sticky=(tk.W, tk.E), padx=20, pady=(0, 10))
        section.columnconfigure(1, weight=1)
        
        ttk.Label(section, text="진행 상황:", style='Section.TLabel').grid(
            row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        # 진행 상태 텍스트
        self.status_label = ttk.Label(section, text="대기 중...", foreground=COLORS['text_light'])
        self.status_label.grid(row=0, column=1, sticky=tk.E, pady=(0, 5))
        
        # 진행 바
        self.progress = ttk.Progressbar(section, mode='determinate', length=400)
        self.progress.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 5))
        
        # 상세 정보
        self.detail_label = ttk.Label(section, text="", foreground=COLORS['text_light'],
                                     font=('Segoe UI', 8))
        self.detail_label.grid(row=2, column=0, columnspan=2, sticky=tk.W)
    
    def create_log_section(self, parent):
        """로그 섹션 생성"""
        section = tk.Frame(parent, bg=COLORS['bg'])
        section.grid(row=5, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=20, pady=(10, 15))
        section.columnconfigure(0, weight=1)
        section.rowconfigure(1, weight=1)
        
        ttk.Label(section, text="다운로드 로그:", style='Section.TLabel').grid(
            row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        # 스크롤바 추가
        scrollbar = ttk.Scrollbar(section)
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        
        self.log_text = tk.Text(section, height=10, width=70, font=("Consolas", 8),
                               yscrollcommand=scrollbar.set, bg='#ffffff',
                               fg=COLORS['fg'], insertbackground=COLORS['primary'])
        self.log_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.config(command=self.log_text.yview)
        
        # 태그 설정
        self.log_text.tag_config('success', foreground=COLORS['success'])
        self.log_text.tag_config('error', foreground=COLORS['danger'])
        self.log_text.tag_config('info', foreground=COLORS['primary'])
        self.log_text.tag_config('warning', foreground=COLORS['warning'])
    
    def log(self, message, tag='info'):
        """로그 메시지 출력"""
        self.log_text.insert(tk.END, message + "\n", tag)
        self.log_text.see(tk.END)
        self.root.update()
    
    def update_status(self, status, detail=""):
        """진행 상태 업데이트"""
        self.status_label.config(text=status)
        if detail:
            self.detail_label.config(text=detail)
        self.root.update()
    
    def update_progress(self, percent, detail=""):
        """진행 바 업데이트"""
        self.progress['value'] = percent
        detail_text = f"{percent:.1f}% " if percent > 0 else ""
        if detail:
            detail_text += detail
        self.detail_label.config(text=detail_text)
        self.root.update()
    
    def browse_folder(self):
        """폴더 선택 대화상자"""
        folder = filedialog.askdirectory(title="저장할 폴더 선택")
        if folder:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder)
    
    def reset_path(self):
        """경로 초기화"""
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, DEFAULT_DOWNLOAD_PATH)
        self.log_text.delete(1.0, tk.END)
    
    def download_video(self, url, output_path, audio_only=False, include_subtitle=False):
        """유튜브 동영상 또는 음성 다운로드"""
        try:
            os.makedirs(output_path, exist_ok=True)
            
            # 기본 포맷 설정
            if audio_only:
                format_str = 'bestaudio/best'
            else:
                format_str = 'best[ext=mp4]/best'
            
            ydl_opts = {
                'format': format_str,
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                'quiet': False,
                'no_warnings': False,
                'progress_hooks': [self.progress_hook],
                'socket_timeout': 30,
            }
            
            # 자막 옵션
            if include_subtitle and not audio_only:
                ydl_opts['writesubtitles'] = True
                ydl_opts['subtitleslangs'] = ['ko', 'en', 'ja', '-live_chat']
                ydl_opts['postprocessors'] = []
            
            # 음성 추출 옵션
            if audio_only:
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                self.log(f"다운로드 시작: {url}", 'info')
                ydl.download([url])
            
            return True, "다운로드 완료!"
        except Exception as e:
            return False, f"오류: {str(e)}"
    
    def progress_hook(self, d):
        """다운로드 진행 상황 표시"""
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate', 0)
            downloaded_bytes = d.get('downloaded_bytes', 0)
            
            if total_bytes > 0:
                percent = (downloaded_bytes / total_bytes) * 100
                self.update_progress(percent, d.get('_speed_str', 'N/A'))
            
            filename = d.get('filename', 'Unknown')
            if filename:
                filename = os.path.basename(filename)
                self.update_status(f"다운로드 중: {filename[:40]}")
        
        elif d['status'] == 'finished':
            self.progress['value'] = 100
            self.update_status("다운로드 완료, 후처리 중...")
            self.log("다운로드 완료, 후처리 중...", 'info')
        
        elif d['status'] == 'error':
            self.log(f"오류: {d.get('error', 'Unknown error')}", 'error')
            self.update_status("오류 발생!")
    
    
    def start_download(self):
        """다운로드 시작"""
        url = self.url_entry.get().strip()
        output_path = self.path_entry.get().strip()
        audio_only = self.download_type.get() == "audio"
        include_subtitle = self.subtitle_var.get()
        
        if not url:
            messagebox.showerror("오류", "YouTube URL을 입력하세요.")
            return
        
        if not output_path:
            messagebox.showerror("오류", "저장 경로를 지정하세요.")
            return
        
        # 다운로드 모드 표시
        mode = "음성" if audio_only else "동영상"
        self.log_text.delete(1.0, tk.END)
        
        self.log(f"[다운로드 시작]", 'info')
        self.log(f"타입: {mode}", 'info')
        self.log(f"URL: {url}", 'info')
        self.log(f"저장 경로: {output_path}", 'info')
        if include_subtitle and not audio_only:
            self.log("자막: 포함됨 (한국어, 영어 등)", 'info')
        self.log("-" * 60, 'info')
        
        # 진행 바 초기화
        self.progress['value'] = 0
        self.update_status("준비 중...")
        self.detail_label.config(text="")
        
        # 다운로드 버튼 비활성화
        self.download_btn.config(state=tk.DISABLED)
        
        # 별도 스레드에서 다운로드
        def download_thread():
            success, message = self.download_video(url, output_path, audio_only, include_subtitle)
            if success:
                self.log(f"\n✓ {message}", 'success')
                self.log(f"저장 경로: {output_path}", 'success')
                self.progress['value'] = 100
                self.update_status("완료!", "모든 파일이 성공적으로 다운로드되었습니다.")
                messagebox.showinfo("완료", message)
            else:
                self.log(f"\n✗ {message}", 'error')
                self.update_status("오류 발생!", message)
                messagebox.showerror("오류", message)
            
            # 다운로드 버튼 활성화
            self.download_btn.config(state=tk.NORMAL)
        
        thread = threading.Thread(target=download_thread, daemon=True)
        thread.start()

def main():
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
