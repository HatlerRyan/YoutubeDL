from pytube import Channel, YouTube
from tkinter import messagebox


def video_only(self):
    yt = YouTube(self)
    video_title = yt.title
    print(video_title)
    messagebox.askyesno(title="video confirmation",
                        message=f"Is this the video you want to download?\n"
                                f"{video_title}")

