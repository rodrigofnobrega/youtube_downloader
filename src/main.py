from pytube import YouTube
from multiprocessing import Process
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_merge_video_audio
import asyncio
from utils.info_video import InfoVideo
from download import Download


async def Convert(yt: YouTube):
    print("Convertendo")
    download_video = asyncio.create_task(DownloadVideo(yt))
    download_audio = asyncio.create_task(DownloadAudio(yt))

    await download_video, download_audio

    output_audio = "audio.mp3"

    videoclip = VideoFileClip("video.mp4")
    audioclip = AudioFileClip("audio.mp4")
    file = audioclip.write_audiofile(output_audio)

    print(file)

    ffmpeg_merge_video_audio(video=videoclip.filename, audio=output_audio, output="audiovideo.mp4")
    '''new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile("audiovideo.mp4", threads=4)'''

async def DownloadVideo(yt: YouTube):
    print("Downloading Video")
    yt.streams.filter(adaptive=True, file_extension="mp4").first().download(filename="video.mp4")

async def DownloadAudio(yt: YouTube):
    print("Downloading Audio")
    yt.streams.filter(adaptive=True, file_extension="mp4", only_audio=True).first().download(filename="audio.mp4")

def main() -> None:
    print('''=======YOUTUBE DOWNLOADER=======\n''')
    
    video_link: str = "https://www.youtube.com/watch?v=K-a8s8OLBSE"

    yt: YouTube = YouTube(video_link)

    output_path: str = "/home/rods/code/python/youtube_downloader/" 

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