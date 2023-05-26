class InfoVideo:
    __video_title: str = None
    __file_path: str = None
    __download_path: str = None
    __only_audio: bool = None
    __only_video: bool = None
    __adaptive: bool = None

    def __init__(self) -> None:    
        pass

    # Setters
    def set_video_title(self, __video_title: str) -> None:
        self.__video_title = __video_title
    
    def set_download_path(self, __download_path: str) -> None:
        self.__download_path = __download_path
    
    def set_only_audio(self, __only_audio: bool) -> None:
        self.__only_audio = __only_audio

    def set_only_video(self, __only_video: bool) -> None:
        self.__only_video = __only_video

    def set_adaptive(self, __adaptive: bool) -> None:
        self.__adaptive = __adaptive

    def set_file_path(self) -> None:
        self.__file_path = str("{download_path}{video_title}").format(download_path=self.__download_path, video_title=self.__video_title)

    # Getters
    def get_video_title(self) -> str:
        return self.__video_title

    def get_file_path(self) -> str:
        return self.__file_path 
    
    def get_download_path(self) -> str:
        return self.__download_path 
    
    def get_only_audio(self) -> bool:
        return self.__only_audio 

    def get_only_video(self) -> bool:
        return self.__only_video 

    def get_adaptive(self) -> bool:
        return self.__adaptive 

    def getVideoInfos(self):
        return {
                    "audio_extension": ".mp3",
                    "video_extension": ".mp4",
                    "filepath": self.__file_path,
                    "download_path": self.__download_path,
                    "only_audio": self.__only_audio,
                    "only_video": self.__only_video,
                    "adaptive": self.__adaptive
                }
    