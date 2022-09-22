from pytube import Channel, YouTube
from tkinter import messagebox, Toplevel, Radiobutton, Checkbutton, Button, StringVar, Label


def selected_type(youtube_list, req_video_type):
    if req_video_type == 'music':
        for vid in youtube_list:
            yt = YouTube(vid)
            stream = yt.streams.get_by_itag(140)
            stream.download('music_downloads')
        print("done")
    elif req_video_type == 'video':
        for vid in youtube_list:
            yt = YouTube(vid)
            stream = yt.streams.get_by_itag(140)
            stream.download('video_downloads')
        print("done")
    elif req_video_type == 'podcast':
        for vid in youtube_list:
            yt = YouTube(vid)
            stream = yt.streams.get_by_itag(140)
            stream.download('podcast_downloads')
        print("done")


class ChannelList:
    youtube_urls = []

    def __init__(self):
        self.video_variable = StringVar()
        # self.youtube_urls = []
        self.checked_text = ''

    def selected_video(self):
        if self.video_variable.get() == '0':
            pass
        elif self.video_variable.get() in self.youtube_urls:
            pass
        else:
            self.youtube_urls.append(self.video_variable.get())
        # print(self.youtube_urls)

    def video_list(self, url, number, channel_window):
        self.checked_text = url
        videos = Checkbutton(channel_window, text=YouTube(url).title, variable=self.video_variable,
                             onvalue=self.checked_text,
                             tristatevalue='tri',
                             command=lambda: ChannelList.selected_video(self))
        videos.grid(row=number, column=0, sticky='w')

    def next_button(self):
        self.download_selected_videos()

    def download_selected_videos(self):
        for url in self.youtube_urls:
            pass

    def select_type(self):
        channel_type_window = Toplevel()
        channel_type_window.title('Type selection')
        channel_type_window.config(width=200, padx=20, pady=20)
        self.type_select = StringVar(None, value="Music")
        music = Radiobutton(channel_type_window, text="Music", variable=self.type_select, value="music")
        video = Radiobutton(channel_type_window, text='Video', variable=self.type_select, value="video")
        podcast = Radiobutton(channel_type_window, text='Podcast', variable=self.type_select, value="podcast")
        type_label = Label(channel_type_window, text="Download as:")
        type_label.grid(column=0, row=0, sticky="w")
        video.grid(column=0, row=1, sticky="w")
        music.grid(column=0, row=2, sticky="w")
        podcast.grid(column=0, row=3, sticky="w")
        download_button = Button(channel_type_window, text='Download',
                                 command=lambda: selected_type(youtube_list=self.youtube_urls,
                                                               req_video_type=self.type_select.get()))
        download_button.grid(column=0, row=4, sticky='w')


def video_only(url):
    yt = YouTube(url)
    video_title = yt.title
    video_confirmation_mb = messagebox.askyesno(title="video confirmation",
                                                message=f"Is this the video you want to download?\n"
                                                        f"{video_title}")
    if video_confirmation_mb:
        video_audio_mb = messagebox.askyesno(title="video or audio",
                                             message="Do you want audio only?")
        print(video_audio_mb)
        if video_audio_mb:
            stream = yt.streams.get_by_itag(140)
            music_podcast_mb = messagebox.askyesno(title="music or podcast",
                                                   message="Is this music?")
            if music_podcast_mb:
                stream.download('music_downloads')
                print("Jam on!")
            elif not music_podcast_mb:
                stream.download('podcast_downloads')
                print("It's in the podcast folder, but it's not really a podcast is it?")
        elif not video_audio_mb:
            stream = yt.streams.get_by_itag(22)
            stream.download('video_downloads')
            print("It's in the video folder")


def chanel_only(url):
    url_list = []
    c = Channel(url)
    channel_window = Toplevel()
    channel_window.title('Last 10 videos')
    len_url_list = len(url_list)

    for url in c.video_urls[:10]:
        url_list.append(url)
        len_url_list = len(url_list)
        video = ChannelList()
        video.video_list(url=url, number=len_url_list, channel_window=channel_window)
    next_button = Button(channel_window, text='Next', command=video.select_type)
    next_button.grid(column=0, row=len_url_list + 1)

