from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root = Tk()
root.title("Black Board")
root.geometry("1050x570+150+50")
root.configure(bg="#79797a")
root.resizable(False, False)

current_x = 0
current_y = 0
color = 'black'
brush_size = 10
eraser_on = False

def locate_xy(work):
    global current_x, current_y
    current_x = work.x
    current_y = work.y

def add_line(work):
    global current_x, current_y, brush_size
    draw_color = 'white' if eraser_on else color
    canvas.create_line((current_x, current_y, work.x, work.y), width=brush_size, fill=draw_color, capstyle=ROUND, smooth=True)
    current_x, current_y = work.x, work.y

def show_color(new_color):
    global color, eraser_on
    color = new_color
    eraser_on = False

def new_canvas():
    canvas.delete('all')

def use_eraser():
    global eraser_on
    eraser_on = True

colors = Canvas(root, bg="#ffffff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

def display_palette():
    color_options = ['black', 'white', 'gray', 'brown4', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']
    for i, col in enumerate(color_options):
        id = colors.create_rectangle((10, 10 + 30*i, 30, 30 + 30*i), fill=col)
        colors.tag_bind(id, '<Button-1>', lambda x, col=col: show_color(col))

display_palette()

canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2") 
canvas.place(x=100, y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', add_line)

current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_changed(event):
    global brush_size
    brush_size = current_value.get()
    value_label.configure(text=get_current_value())

slider = ttk.Scale(root, from_=1, to=20, orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

eraser_button = Button(root, text="Eraser", command=use_eraser)
eraser_button.place(x=30, y=10)

clear_button = Button(root, text="Clear All", command=new_canvas)
clear_button.place(x=30, y=40)

root.mainloop()
