from pytube import YouTube
from src.modules.utils.info_video import InfoVideo
from src.modules.download import Download

def main() -> None:
    print('''=======YOUTUBE DOWNLOADER=======\n''')
    
    video_link: str = str(input("Video link: "))

    yt: YouTube = YouTube(video_link)

    output_path: str =  str(input("Download directory: "))

    info_video: InfoVideo = InfoVideo()
    info_video.set_filename_sufix(".mp3")
    info_video.set_video_title(yt.title)
    info_video.set_output_path(output_path)
    info_video.set_only_audio(True)
    info_video.set_only_video(False)
    info_video.set_adaptive(True)
    info_video.set_filename()

    downloader: Download = Download(yt=yt, only_audio=info_video.get_only_audio(), only_video=info_video.get_only_video(), adaptive=info_video.get_adaptive(), output_path=info_video.get_output_path(), filename=info_video.get_filename())

    downloader.Downloader()
    

if __name__ == "__main__":
    main()