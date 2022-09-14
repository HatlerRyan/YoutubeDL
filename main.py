
from tkinter import *


window = Tk()
window.title("YoutubeDL")
window.config(width=500, height=500, pady=20, padx=20)
url_text = Label(text="URL of:")
url_text.grid(column=0, row=0, columnspan=2)
channel_or_video = StringVar(None, "video")
channel = Radiobutton(text="Channel", variable=channel_or_video, value="channel")
video = Radiobutton(text='Video', variable=channel_or_video, value="video")
channel.grid(column=0, row=1, sticky="e")
video.grid(column=1, row=1, sticky="w")
url_entry = Entry(width=30)
url_entry.focus()

url_entry.grid(column=0, row=4,columnspan=2)

next_button = Button(text="Next",)
next_button.grid(column=0,row=6, columnspan=2, pady=5)



window.mainloop()
