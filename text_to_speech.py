from tkinter import *
from gtts import gTTS
import os

t = Tk()

frame1 = Frame(t,bg = "orange",height = "150")
frame1.pack(fill = X)


frame2 = Frame(t,bg = "green",height = "750")
frame2.pack(fill=X)

label = Label(frame1, text = "Text to Speech",font = "bold, 30",bg = "orange")

label.place(x = 180, y = 70)

entry = Entry(frame2, width = 45,bd = 4, font = 14)

entry.place(x = 70, y = 60)
entry.insert(0, "")


def play():

    language = "en"
    myobj = gTTS(text = entry.get(),lang = language,slow = False)

    obj.save("convert.wav")
    os.system("convert.wav")

btn = Button(frame2, text = "SUBMIT",width = "15", pady = 10,font = "bold, 15",command = play, bg='blue')

btn.place(x = 250,y = 130)

t.title("text_to_speech_convertor")

t.geometry("650x550+350+200")

t.mainloop()
