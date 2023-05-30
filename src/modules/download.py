from sys import stdout
from typing import Any
from pytube import YouTube, Stream

class Download:
    __yt: YouTube = None
    __output_path: str = None
    __filename: str = None
    __file_path: str = None
    __stream: Stream = None

    def __init__(self, yt: YouTube, output_path: str, filename: str) -> None:
        self.__yt = yt
        self.__output_path = output_path
        self.__filename = filename

    def bar_download_progress(self, chunk, file_handle, bytes_remaining: bytes):
        filesize = self.__stream.filesize
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
'''.format(output_path=self.__output_path, filename=self.__filename, filesize=self.__stream.filesize_mb))
        
    def downloader(self, only_audio: bool=False, only_video: bool=False, adaptive: bool=True):
        self.__stream = self.__yt.streams.filter(file_extension="mp4", only_audio=only_audio, only_video=only_video, adaptive=adaptive).first()

        self.__yt.register_on_progress_callback(self.bar_download_progress)
        self.__yt.register_on_complete_callback(self.info_about_download)
        
        self.__stream.download(output_path=self.__output_path, filename=self.__filename)

