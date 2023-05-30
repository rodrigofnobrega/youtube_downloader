from moviepy.editor import AudioFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_merge_video_audio

class Convert:

    def __init__(self) -> None:
        pass

    def convert_to_mp3(self, filepath: str) -> None:
        self.audioclip = AudioFileClip(filepath)
        self.audioclip.write_audiofile(filepath+".mp3")

    def merge_video_audio(self, video_file: str, audio_file_path: str, output_file: str) -> None:
        ffmpeg_merge_video_audio(video=video_file, audio=audio_file_path, output=output_file)
