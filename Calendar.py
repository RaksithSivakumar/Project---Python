from tkinter import *
from tkcalendar import Calendar


root = Tk()
root.geometry("300x300")
root.title("Calendar")
root.configure(bg="lightblue")


def selectDate():
    mydate = mycal.get_date()
    select_date_label.config(text=f"Selected Date: {mydate}")


mycal = Calendar(root, setmode="day", date_pattern='d/m/yy')
mycal.pack(padx=15, pady=15)


open_cal = Button(root, text="Select Date", command=selectDate)
open_cal.pack(padx=15, pady=15)


select_date_label = Label(root, text="", bg="lightblue", font=("Arial", 12))
select_date_label.pack(padx=15, pady=15)


root.mainloop()
