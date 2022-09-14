
from tkinter import *


window = Tk()
window.title("YoutubeDl")
window.config(width=500, height=500, pady=50,padx=50)
url_entry = Entry()
url_entry.focus()

url_entry.grid(column=0, row=0)



window.mainloop()
