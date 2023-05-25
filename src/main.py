from pytube import YouTube
from utils.info_video import InfoVideo
from modules.download import Download

def main() -> None:
    print('''=======YOUTUBE DOWNLOADER=======\n''')
    
    video_link: str = str(input("Video link: "))

    yt: YouTube = YouTube(video_link)

    output_path: str =  str(input("Download directory: "))

    info_video: InfoVideo = InfoVideo()
    info_video.set_filename_sufix(".mp4")
    info_video.set_video_title(yt.title)
    info_video.set_output_path(output_path)
    info_video.set_only_audio(False)
    info_video.set_only_video(True)
    info_video.set_adaptive(True)
    info_video.set_filename()

    downloader: Download = Download(yt=yt, output_path=info_video.get_output_path(), filename=info_video.get_filename())

    downloader.downloader(only_audio=info_video.get_only_audio(), only_video=info_video.get_only_video(), adaptive=info_video.get_adaptive())

if __name__ == "__main__":
    main()