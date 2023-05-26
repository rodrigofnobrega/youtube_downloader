from pytube import YouTube
from utils.info_video import InfoVideo
from modules.download import Download
from modules.convert import Convert

def main() -> None:
    print('''=======YOUTUBE DOWNLOADER=======\n''')
    
    video_link: str = str(input("Video link: "))
    download_path: str =  str(input("Download directory: "))
    
    yt: YouTube = YouTube(video_link)

    info_video: InfoVideo = InfoVideo()
    info_video.set_video_title(yt.title)
    info_video.set_download_path(download_path)
    info_video.set_only_audio(True)
    info_video.set_only_video(False)
    info_video.set_adaptive(True)
    info_video.set_file_path()

    downloader: Download = Download(yt=yt, output_path=download_path, filename=info_video.get_file_path())

    downloader.downloader(only_audio=info_video.get_only_audio(), only_video=info_video.get_only_video(), adaptive=info_video.get_adaptive())

    convert: Convert = Convert()

    convert.convert_audio(filepath=info_video.get_file_path(), filename=info_video.get_filename())

if __name__ == "__main__":
    main()