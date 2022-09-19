from pytube import Channel, YouTube
from tkinter import messagebox, Tk, Radiobutton, StringVar



class ChannelList:
    def __init__(self, url):
        self.url = url
        # self.title = title
        self.video_variable = StringVar(None)
        self.video_list_value = self.video_variable.get()
        self.video_num = 0
#
    def selected_video(self):
        print(self.video_list_value)

    def video_list(self, video_number):
        video_label =
# #         video = Radiobutton(text="Channel", variable=variable, value=video_num, command=selected_video)
# #         # video = Radiobutton(text='Video', variable=self.video_list, value="video", command=self.selected_video)
# #         video.pack()
# #         self.video_num += 1



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
    video_url = []
    video_num = 0
    c = Channel(url)
    # print(c)
    channel_window = Tk()
    channel_window.title('Last 10 videos')

    for url in c.video_urls[:10]:
        ChannelList.video_list(url, video_num)
    #     video_url.append(url)
    #     print(f'{video_num} {YouTube(url).title}')
    #     video_num += 1
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
    channel_window.mainloop()
