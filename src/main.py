from os import remove
from pytube import YouTube
from utils.info_video import InfoVideo
from modules.download import Download
from modules.convert import Convert

def main() -> None:
    print('''=======YOUTUBE DOWNLOADER=======\n''')
    
    video_link: str = str(input("Video link: "))

    download_dir: str =  str(input("Download directory: "))

    type_download: int = int(input('''[0] => Download Audio
[1] => Download Video
Type of download: '''))
    
    while True:
        yt: YouTube = YouTube(video_link)

        info_video: InfoVideo = InfoVideo()
        info_video.set_video_title(yt.title)
        info_video.set_download_dir(download_dir)
        info_video.set_file_path(download_dir, yt.title)

        downloader: Download = Download(yt=yt, output_path=download_dir, filename=yt.title)
        convert: Convert = Convert()

        if type_download == 0:
            downloader.downloader(only_audio=True)
            convert.convert_to_mp3(filepath=info_video.get_file_path())

        else:
            downloader.downloader(only_audio=True)
            convert.convert_to_mp3(filepath=info_video.get_file_path())
            
            downloader.downloader(only_video=True)
            convert.merge_video_audio(video_file=info_video.get_file_path(), audio_file_path=info_video.get_file_path()+".mp3", output_file=info_video.get_file_path()+".mp4")
            
            remove(info_video.get_file_path()+".mp3")

        remove(info_video.get_file_path())

        video_link = str(input("Video link: "))

if __name__ == "__main__":
    main()