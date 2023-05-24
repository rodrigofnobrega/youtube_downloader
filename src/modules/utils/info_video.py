class InfoVideo:
    filename_sufix: str = None
    video_title: str = None
    filename: str = None
    output_path: str = None
    only_audio: bool = None
    only_video: bool = None
    adaptive: bool = None

    def __init__(self) -> None:    
        pass

    # Setters
    def set_filename_sufix(self, filename_sufix: str) -> None:
        self.filename_sufix = filename_sufix

    def set_video_title(self, video_title: str) -> None:
        self.video_title = video_title
    
    def set_output_path(self, output_path: str) -> None:
        self.output_path = output_path
    
    def set_only_audio(self, only_audio: bool) -> None:
        self.only_audio = only_audio

    def set_only_video(self, only_video: bool) -> None:
        self.only_video = only_video

    def set_adaptive(self, adaptive: bool) -> None:
        self.adaptive = adaptive

    def set_filename(self) -> None:
        self.filename = str("{video_title}{filename_sufix}").format(video_title=self.video_title, filename_sufix=self.filename_sufix)

    # Getters
    def get_filename_sufix(self) -> str:
        return self.filename_sufix 

    def get_video_title(self) -> str:
        return self.video_title

    def get_filename(self) -> str:
        return self.filename 
    
    def get_output_path(self) -> str:
        return self.output_path 
    
    def get_only_audio(self) -> bool:
        return self.only_audio 

    def get_only_video(self) -> bool:
        return self.only_video 

    def get_adaptive(self) -> bool:
        return self.adaptive 


    def getVideoInfos(self):
        return {
                    "filename_sufix": self.filename_sufix,
                    "filename": self.filename,
                    "output_path": self.output_path,
                    "only_audio": self.only_audio,
                    "only_video": self.only_video,
                    "adaptive": self.adaptive
                }

    