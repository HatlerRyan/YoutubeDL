from pytube import Channel, YouTube
from tkinter import messagebox, Tk, Radiobutton, StringVar, Toplevel, IntVar, Checkbutton




class ChannelList:
    def __init__(self):
        self.video_variable = IntVar()

    def selected_video(self):
        print(self.video_variable)


    def video_list(self, url, number, channel_window):
        videos = Checkbutton(channel_window, text=f' {YouTube(url).title}', variable=self.video_variable)
        videos.grid(row=number, column=0, sticky='w')

    # def video_list(self, url, channel_window, number):
    #     self.rb_value = number
    #     video = Radiobutton(channel_window, text=f' {YouTube(url).title}', variable=self.video_variable,
    #                         value=number, command=self.selected_video)
    #     #
    #     video.grid(row=number, column=0, sticky='w')


def video_only(url):
    yt = YouTube(url)
    video_title = yt.title
    # print(video_title)
    video_confirmation_mb = messagebox.askyesno(title="video confirmation",
                                                message=f"Is this the video you want to download?\n"
                                                        f"{video_title}")
    # video_confirmation_mb
    # print(video_confirmation_mb)
    if video_confirmation_mb:
        video_audio_mb = messagebox.askyesno(title="video or audio",
                                             message="Do you want audio only?")
        print(video_audio_mb)
        if video_audio_mb:
            stream = yt.streams.get_by_itag(140)
            music_podcast_mb = messagebox.askyesno(title="music or podcast",
                                                   message="Is this music?")
            music_podcast_mb
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
    loop_num = 0
    channel_url = url
    c = Channel(url)
    channel_window = Toplevel()
    channel_window.title('Last 10 videos')

    for url in c.video_urls[:5]:
        url_list.append(url)
        len_url_list = len(url_list)
        video = ChannelList()
        video.video_list(url=url, number=len_url_list, channel_window=channel_window)
    # ChannelList.selected_video()
    # selections = input('Select videos you wish to download. ').split()
    # audio_only_question = input('Do you want audio only? y/n ')
    # for download in selections:
    #     yt = YouTube(video_url[int(download)])
    #     if audio_only_question == 'y':
    #         stream = yt.streams.get_by_itag(140)
    #         download_question = input("Is this music or a podcast? m/p ")
    #         if download_question == 'm':
    #             stream.download('music_downloads')
    #         elif download_question == 'p':
    #             stream.download('podcast_downloads')
    #     elif audio_only_question == 'n':
    #         stream = yt.streams.get_by_itag(22)
    #         stream.download('video_downloads')
