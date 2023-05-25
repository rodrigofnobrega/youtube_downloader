from sys import stdout
from typing import Any
from pytube import YouTube, Stream

class Download:
    yt: YouTube = None
    only_audio: bool = None
    only_video: bool = None
    adaptive: bool = None
    output_path: str = None
    filename: str = None
    stream: Stream = None

    def __init__(self, yt: YouTube, only_audio: bool, only_video: bool, adaptive: bool, output_path: str, filename: str) -> None:
        self.yt = yt
        self.only_audio = only_audio
        self.only_video = only_video
        self.adaptive = adaptive
        self.output_path = output_path
        self.filename = filename

    def bar_download_progress(self, chunk, file_handle, bytes_remaining: bytes):
        filesize = self.stream.filesize
        current = ((filesize - bytes_remaining) / filesize)
        percent = ('{0:.1f}').format(current * 100)
        progress = int(50 * current)
        status = '█' * progress + '-' * (50 - progress)
        stdout.write('↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
        stdout.flush()

    def info_about_download(self, stream: Stream, file_path: str):
        print('''\n
        =======Download Complete=======
        Output path => {output_path}
        File name => {filename}
        File size => {filesize}Mb
        '''.format(output_path=self.output_path, filename=self.filename, filesize=self.stream.filesize_mb))
        
    def downloader(self):
        self.stream = self.yt.streams.filter(file_extension="mp4", only_audio=self.only_audio, only_video=self.only_video, adaptive=self.adaptive).first()

        self.yt.register_on_progress_callback(self.bar_download_progress)
        self.yt.register_on_complete_callback(self.info_about_download)
        
        self.stream.download(output_path=self.output_path, filename=self.filename)
        