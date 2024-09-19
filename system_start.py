import os
import tkinter as tk
from tkinter import messagebox

def shutdown():
    response = messagebox.askyesno("Shutdown", "Are you sure you want to shutdown?")
    if response:
        os.system("shutdown /s /t 1")

def restart():
    response = messagebox.askyesno("Restart", "Are you sure you want to restart?")
    if response:
        os.system("shutdown /r /t 1")

def logout():
    response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if response:
        os.system("shutdown -l")

root = tk.Tk()
root.title("Shutdown, Restart, Logout")
root.geometry("300x200")

shutdown_button = tk.Button(root, text="Shutdown", command=shutdown, width=15, height=2)
restart_button = tk.Button(root, text="Restart", command=restart, width=15, height=2)
logout_button = tk.Button(root, text="Logout", command=logout, width=15, height=2)

shutdown_button.pack(pady=10)
restart_button.pack(pady=10)
logout_button.pack(pady=10)

root.mainloop()
