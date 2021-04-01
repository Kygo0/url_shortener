import pyshorteners as pr
from tkinter import *
from tkinter.ttk import *

root = Tk()
e = Entry(root, width=50)
e.pack()
root.title("URL SHORTENER")


def shorten(master: Tk):
    link = e.get()
    shortener = pr.Shortener()
    Short_Link = shortener.tinyurl.short(link)
    master.clipboard_append(Short_Link)
    master.update()
    Label1 = Label(root, text=Short_Link)
    Label2 = Label(root, text="COPIED TO CLIPBOARD!")
    Label1.pack()
    Label2.pack()


Button1 = Button(root, text="Enter link:", command=lambda: shorten(root))
Button1.pack()

root.mainloop()
