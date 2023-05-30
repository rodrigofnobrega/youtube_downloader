class InfoVideo:
    __video_title: str = None
    __file_path: str = None
    __download_dir: str = None
    __only_audio: bool = None
    __only_video: bool = None
    __adaptive: bool = None

    def __init__(self) -> None:    
        pass

    # Setters
    def set_video_title(self, video_title: str) -> None:
        self.__video_title = video_title
    
    def set_download_dir(self, download_dir: str) -> None:
        self.__download_dir = download_dir
    
    def set_only_audio(self, only_audio: bool) -> None:
        self.__only_audio = only_audio

    def set_only_video(self, only_video: bool) -> None:
        self.__only_video = only_video

    def set_adaptive(self, adaptive: bool) -> None:
        self.__adaptive = adaptive

    def set_file_path(self, download_dir: str, video_title: str) -> None:
        self.__file_path = download_dir+"/"+video_title

    # Getters
    def get_video_title(self) -> str:
        return self.__video_title

    def get_file_path(self) -> str:
        return self.__file_path 
    
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
                    "video_title": self.__video_title,
                    "file_path": self.__file_path,
                    "download_dir": self.__download_dir,
                    "only_audio": self.__only_audio,
                    "only_video": self.__only_video,
                    "adaptive": self.__adaptive
                }

