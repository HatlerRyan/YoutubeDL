from pytube import YouTube
def get_url():
    yt = YouTube(input("What's the URL? "))
    video_title = yt.title
    print(video_title)
    return yt

def audio_only(yt):
    audio_only_question = input('Do you want audio only? y/n ')
    if audio_only_question == 'y':
        # audio_only = yt.streams.filter(only_audio=True)
        # for stream in audio_only:
        # print(stream)
        stream = yt.streams.get_by_itag(140)
        # print(stream)
        download_question = input("Is this music or a podcast? m/p ")
        if download_question == 'm':
            stream.download('C:\\Users\\hatle\\Documents\\Fun\\Music')
        elif download_question == 'p':
            stream.download('C:\\Users\\hatle\\Documents\\Fun\\podcast')
    elif audio_only_question == 'n':
        for stream in yt.streams.filter(progressive=True):
            # print(stream)
            stream = yt.streams.get_by_itag(22)
            stream.download('C:\\Users\\hatle\\Documents\\Fun\\videos')


