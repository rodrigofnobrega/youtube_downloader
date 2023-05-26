class InfoVideo:
    __video_title: str = None
    __filepath: str = None
    __download_dir: str = None
    __only_audio: bool = None
    __only_video: bool = None
    __adaptive: bool = None

    def __init__(self) -> None:    
        pass

    # Setters
    def set_video_title(self, __video_title: str) -> None:
        self.__video_title = __video_title
    
    def set_download_dir(self, __download_dir: str) -> None:
        self.__download_dir = __download_dir
    
    def set_only_audio(self, __only_audio: bool) -> None:
        self.__only_audio = __only_audio

    def set_only_video(self, __only_video: bool) -> None:
        self.__only_video = __only_video

    def set_adaptive(self, __adaptive: bool) -> None:
        self.__adaptive = __adaptive

    def set_file_path(self) -> None:
        self.__filepath = str("{download_dir}{video_title}").format(download_dir=self.__download_dir, video_title=self.__video_title)

    # Getters
    def get_video_title(self) -> str:
        return self.__video_title

    def set_file_path(self) -> str:
        return self.__filepath 
    
    def get_download_dir(self) -> str:
        return self.__download_dir 
    
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
    