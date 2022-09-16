from pytube import Channel, YouTube
from tkinter import messagebox


def video_only(self):
    yt = YouTube(self)
    video_title = yt.title
    print(video_title)
    video_confirmation_mb = messagebox.askyesno(title="video confirmation",
                        message=f"Is this the video you want to download?\n"
                                f"{video_title}")
    video_confirmation_mb
    if video_confirmation_mb:
        video_audio_mb = messagebox.askyesno(title="video or audio",
                            message="Do you want audio only?")
        video_audio_mb
        if video_audio_mb:
            stream = yt.streams.get_by_itag(140)
            music_podcast_mb = messagebox.askyesno(title="music or podcast",
                            message="Is this music?")
            music_podcast_mb
            if music_podcast_mb:
                stream.download('music_downloads')
                print("You did it")


