import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def resize_images(input_folder, output_folder, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            try:
                img = Image.open(os.path.join(input_folder, filename))
                img = img.resize((width, height), Image.ANTIALIAS)
                img.save(os.path.join(output_folder, filename))
            except Exception as e:
                print(f"Error resizing image {filename}: {e}")

def select_input_folder():
    folder = filedialog.askdirectory()
    input_folder_var.set(folder)

def select_output_folder():
    folder = filedialog.askdirectory()
    output_folder_var.set(folder)

def start_resizing():
    input_folder = input_folder_var.get()
    output_folder = output_folder_var.get()
    width = int(width_var.get())
    height = int(height_var.get())
    
    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Please select both input and output folders.")
        return
    
    resize_images(input_folder, output_folder, width, height)
    messagebox.showinfo("Success", "Images have been resized successfully!")


root = tk.Tk()
root.title("Bulk Image Resizer")
root.geometry("400x300")
root.configure(bg="#ececec")

input_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()
width_var = tk.StringVar()
height_var = tk.StringVar()

tk.Label(root, text="Input Folder:", bg="#ececec", font=("Helvetica", 12)).pack(pady=5)
tk.Entry(root, textvariable=input_folder_var, font=("Helvetica", 12), width=30).pack(pady=5)
tk.Button(root, text="Browse", command=select_input_folder, font=("Helvetica", 12), bg="#4CAF50", fg="white").pack(pady=5)

tk.Label(root, text="Output Folder:", bg="#ececec", font=("Helvetica", 12)).pack(pady=5)
tk.Entry(root, textvariable=output_folder_var, font=("Helvetica", 12), width=30).pack(pady=5)
tk.Button(root, text="Browse", command=select_output_folder, font=("Helvetica", 12), bg="#4CAF50", fg="white").pack(pady=5)

tk.Label(root, text="Width:", bg="#ececec", font=("Helvetica", 12)).pack(pady=5)
tk.Entry(root, textvariable=width_var, font=("Helvetica", 12), width=10).pack(pady=5)

tk.Label(root, text="Height:", bg="#ececec", font=("Helvetica", 12)).pack(pady=5)
tk.Entry(root, textvariable=height_var, font=("Helvetica", 12), width=10).pack(pady=5)

tk.Button(root, text="Start Resizing", command=start_resizing, font=("Helvetica", 12), bg="#4CAF50", fg="white").pack(pady=20)

root.mainloop()
