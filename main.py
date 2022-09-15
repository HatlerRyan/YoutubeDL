from tkinter import *
from function_file import SomethingRandom

window = Tk()
window.title("YoutubeDL")
window.config(width=500, height=500, pady=20, padx=20)
url_text = Label(text="URL of:")
url_text.grid(column=0, row=0, columnspan=2)


def selected():
    radiobutton_value = channel_or_video.get()
    return radiobutton_value

def busted_face():
    if selected == 'video':
        messagebox.askquestion("sjkdflsj", "djfksljf")


channel_or_video = StringVar(None, "video")
channel = Radiobutton(text="Channel", variable=channel_or_video, value="channel", command=selected)
video = Radiobutton(text='Video', variable=channel_or_video, value="video", command=selected)

channel.grid(column=0, row=1, sticky="e")
video.grid(column=1, row=1, sticky="w")
url_entry = Entry(width=30)
url_entry.focus()

url_entry.grid(column=0, row=4, columnspan=2)
# next_button_press = SomethingRandom.next_button_press(url_type="help")
what_type = SomethingRandom(url_type=selected())
# print(what_type)

next_button = Button(text="Next", command=busted_face)
next_button.grid(column=0, row=6, columnspan=2, pady=5)




window.mainloop()
