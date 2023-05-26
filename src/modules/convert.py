from moviepy.editor import AudioFileClip

class Convert:

    def __init__(self) -> None:
        pass

    def convert_audio(self, filepath: str, filename: str) -> None:
        output_file: str = str(f"{filepath}/{filename}")

        self.audioclip = AudioFileClip(output_file)
        self.audioclip.write_audiofile(output_file)
