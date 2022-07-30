from pytube import YouTube, Channel
# install pyinstaller

x = input("Specific video or search a channel? v/c ")
if x == 'v':
    yt = YouTube(input("What's the URL? "))
    video_title = yt.title
    print(video_title)
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
        # for stream in yt.streams.filter(progressive=True):
        # print(stream)
        stream = yt.streams.get_by_itag(22)
        stream.download('C:\\Users\\hatle\\Documents\\Fun\\videos')
elif x == 'c':
    channel_question = input('Which channel do you want to search? PMS/HD ').lower()
    video_url = []
    video_num = 0
    if channel_question == "pms":
        c = Channel('https://www.youtube.com/c/ThePatMcAfeeShow/videos')
        for url in c.video_urls[:10]:
            video_url.append(url)
            print(f'{video_num} {YouTube(url).title}')
            video_num += 1
    elif channel_question == "hd":
        c = Channel('https://www.youtube.com/c/HammerDahn/videos')
        for url in c.video_urls[:5]:
            video_url.append(url)
            print(f'{video_num} {YouTube(url).title}')
            video_num += 1
    selections = input('Select videos you wish to download. ').split()
    audio_only_question = input('Do you want audio only? y/n ')
    for download in selections:
        yt = YouTube(video_url[int(download)])


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
            # for stream in yt.streams.filter(progressive=True):
            # print(stream)
            stream = yt.streams.get_by_itag(22)
            stream.download('C:\\Users\\hatle\\Documents\\Fun\\videos')

