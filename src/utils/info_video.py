class InfoVideo:
    __filename_sufix: str = None
    __video_title: str = None
    __filename: str = None
    __output_path: str = None
    __only_audio: bool = None
    __only_video: bool = None
    __adaptive: bool = None

    def __init__(self) -> None:    
        pass

    # Setters
    def set_filename_sufix(self, __filename_sufix: str) -> None:
        self.__filename_sufix = __filename_sufix

    def set_video_title(self, __video_title: str) -> None:
        self.__video_title = __video_title
    
    def set_output_path(self, __output_path: str) -> None:
        self.__output_path = __output_path
    
    def set_only_audio(self, __only_audio: bool) -> None:
        self.__only_audio = __only_audio

    def set_only_video(self, __only_video: bool) -> None:
        self.__only_video = __only_video

    def set_adaptive(self, __adaptive: bool) -> None:
        self.__adaptive = __adaptive

    def set_filename(self) -> None:
        self.__filename = str("{video_title}{filename_sufix}").format(video_title=self.__video_title, filename_sufix=self.__filename_sufix)

    # Getters
    def get_filename_sufix(self) -> str:
        return self.__filename_sufix 

    def get_video_title(self) -> str:
        return self.__video_title

    def get_filename(self) -> str:
        return self.__filename 
    
    def get_output_path(self) -> str:
        return self.__output_path 
    
    def get_only_audio(self) -> bool:
        return self.__only_audio 

    def get_only_video(self) -> bool:
        return self.__only_video 

    def get_adaptive(self) -> bool:
        return self.__adaptive 

    def getVideoInfos(self):
        return {
                    "filename_sufix": self.__filename_sufix,
                    "filename": self.__filename,
                    "output_path": self.__output_path,
                    "only_audio": self.__only_audio,
                    "only_video": self.__only_video,
                    "adaptive": self.__adaptive
                }
    