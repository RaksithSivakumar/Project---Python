import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text to Speech")
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg="#2d545e")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        setvoice()

top_frame = Frame(root, bg="white", width=900, height=100)
top_frame.place(x=0, y=0)

Label(top_frame, text="TEXT TO SPEECH", font="Arial 20 bold", bg="white", fg="black").place(x=100, y=30)

text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text="VOICE", font="Arial 15 bold", bg="#305065", fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="Arial 15 bold", bg="#305065", fg="white").place(x=760, y=160)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="Arial 14", state='readonly', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="Arial 14", state='readonly', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

btn = Button(root, text="Speak", compound=LEFT, width=130, font="Arial 14 bold", command=speaknow)
btn.place(x=550, y=280)

root.mainloop()
