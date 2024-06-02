from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfile
import subprocess
import os

root = Tk()
root.title("Python IDLE")
root.geometry("1280x720+150+80")
root.configure(bg="#323846")
root.resizable(False, False)

file_path = ''

def set_file_path(path):
    global file_path
    file_path = path 

def open_file():
    path = askopenfile(filetypes=[('Python File', '*.py')])
    if path:
        with open(path.name, 'r') as file:
            code = file.read()
            code_input.delete('1.0', END)
            code_input.insert('1.0', code)
            set_file_path(path.name)

def save():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path

    if path:
        with open(path, 'w') as file:
            code = code_input.get('1.0', END)
            file.write(code)
            set_file_path(path)

def run():
    if file_path == '':
        messagebox.showerror("Python IDLE", "Save Your Code")
        return

    command = f'python "{file_path}"'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.delete('1.0', END)
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

def create_circle_button(text, command, x, y):
    canvas = Canvas(root, width=60, height=60, bg="#323846", highlightthickness=0)
    canvas.create_oval(10, 10, 50, 50, fill="#ffffff")
    btn = Button(root, text=text, command=command, bd=0, highlightthickness=0, bg="#ffffff")
    canvas.create_window(30, 30, window=btn)
    canvas.place(x=x, y=y)

create_circle_button("Open", open_file, 30, 30)
create_circle_button("Save", save, 30, 145)
create_circle_button("Run", run, 30, 260)

code_input = Text(root, font="console 18")
code_input.place(x=180, y=0, width=680, height=720)

code_output = Text(root, font="console 15", bg="#323846", fg="lightgreen")
code_output.place(x=860, y=0, width=420, height=720)

root.mainloop()
