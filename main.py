from tkinter import messagebox, Tk, Label, StringVar, Radiobutton, Entry, Button
from function_file import video_only, chanel_only

window = Tk()
window.title("YoutubeDL")
window.config(width=500, height=500, pady=20, padx=20)
url_text = Label(text="URL of:")
url_text.grid(column=0, row=0, columnspan=2)



# -------------functions------------------#


def selected_c_or_v():
    channel_or_video_value = channel_or_video.get()
    return channel_or_video_value

def busted_face():
    url = url_entry.get()
    if selected_c_or_v() == "video":
        video_only(url)
    elif selected_c_or_v() == "channel":
        chanel_only(url)


#------------Program----------#


channel_or_video = StringVar(None, "channel")
channel = Radiobutton(text="Channel", variable=channel_or_video, value="channel", command=selected_c_or_v)
video = Radiobutton(text='Video', variable=channel_or_video, value="video", command=selected_c_or_v)

channel.grid(column=0, row=1, sticky="e")
video.grid(column=1, row=1, sticky="w")
url_entry = Entry(width=30)
url_entry.focus()

url_entry.grid(column=0, row=4, columnspan=2)
# next_button_press = SomethingRandom.next_button_press(url_type="help")
# what_type = SomethingRandom(url_type=selected())
# print(what_type)

next_button = Button(text="Next", command=busted_face)
next_button.grid(column=0, row=6, columnspan=2, pady=5)




window.mainloop()
