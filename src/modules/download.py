from typing import Any
from pytube import YouTube

class Download:
    yt: YouTube = None
    only_audio: bool = None
    only_video: bool = None
    adaptive: bool = None
    output_path: str = None
    filename: str = None


    def __init__(self, yt: YouTube, only_audio: bool, only_video: bool, adaptive: bool, output_path: str, filename: str) -> None:
        self.yt = yt
        self.only_audio = only_audio
        self.only_video = only_video
        self.adaptive = adaptive
        self.output_path = output_path
        self.filename = filename

    def Downloader(self):
        self.yt.streams.filter(file_extension="mp4", only_audio=self.only_audio, only_video=self.only_video, adaptive=self.adaptive).first().download(output_path=self.output_path, filename=self.filename)
        

