import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tk_file
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.geometry('500x500')
root.title('Tkinter Hub')

def popup_menu(e):
    menu_bar.tk_popup(e.x_root, e.y_root)

image_list = []
image_vars = []

def load_images():
    dir_path = tk_file.askdirectory()

    if not dir_path:
        return

    image_files = os.listdir(dir_path)

    for r in range(len(image_files)):
        file_path = os.path.join(dir_path, image_files[r])
        try:
            img_thumb = ImageTk.PhotoImage(Image.open(file_path).resize((50, 50), Image.LANCZOS))
            img_full = ImageTk.PhotoImage(Image.open(file_path).resize((480, 360), Image.LANCZOS))
            image_list.append((img_thumb, img_full))
            btn = tk.Button(slider, image=img_thumb, command=lambda img=img_full: display_image(img))
            btn.grid(row=0, column=r, padx=5, pady=5)
        except Exception as e:
            print(f"Error loading image {file_path}: {e}")

def display_image(img):
    image_display_lb.config(image=img)
    image_display_lb.image = img

menu_btn = tk.Button(root, text='Menu', bd=0)
menu_btn.pack(side=tk.TOP, anchor=tk.W, pady=20, padx=20)
menu_btn.bind('<Button-1>', popup_menu)

menu_bar = tk.Menu(root, tearoff=False)
menu_bar.add_command(label='Open Folder', command=load_images)

image_display_lb = tk.Label(root)
image_display_lb.pack(anchor=tk.CENTER)

canvas = tk.Canvas(root, height=60, width=500)
canvas.pack(side=tk.BOTTOM, fill=tk.X)

x_scroll_bar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
x_scroll_bar.pack(side=tk.BOTTOM, fill=tk.X)
x_scroll_bar.config(command=canvas.xview)

canvas.config(xscrollcommand=x_scroll_bar.set)
canvas.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox('all')))

slider = tk.Frame(canvas)
canvas.create_window((0, 0), window=slider, anchor=tk.NW)

root.mainloop()
