from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator


root = Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="DARK BLUE")

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    text_ = text1.get(1.0, END)
    t1 = Translator()
    Trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trans_text = Trans_text.text

    text2.delete(1.0, END)
    text2.insert(END, trans_text)


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()


combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("English")

label1 = Label(root, text="ENGLISH", font="Segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo2.place(x=780, y=20)
combo2.set("Select Language")

label2 = Label(root, text="ENGLISH", font="Segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=10, y=118, width=440, height=210)

text1 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

f2 = Frame(root, bg="Black", bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill='y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


translate_button = Button(root, text="Translate", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1, width=10, height=2, bg="black", fg="white", command=translate_now)
translate_button.place(x=476, y=250)

label_change()

root.mainloop()
