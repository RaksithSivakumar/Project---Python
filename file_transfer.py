import os
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil

class FileTransferApp:
    def setup_gui(self, root):
        self.root = root
        self.root.title("File Transfer App")
        self.root.geometry("400x200")
        
        self.source_file = ""
        self.destination_directory = ""
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="File Transfer Application", font=("Helvetica", 16)).pack(pady=10)
        
        tk.Button(self.root, text="Select File", command=self.select_file, font=("Helvetica", 12)).pack(pady=5)
        tk.Button(self.root, text="Select Destination", command=self.select_destination, font=("Helvetica", 12)).pack(pady=5)
        tk.Button(self.root, text="Transfer File", command=self.transfer_file, font=("Helvetica", 12)).pack(pady=10)
        
        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.status_label.pack(pady=5)

    def select_file(self):
        self.source_file = filedialog.askopenfilename()
        if self.source_file:
            self.status_label.config(text=f"Selected File: {os.path.basename(self.source_file)}")

    def select_destination(self):
        self.destination_directory = filedialog.askdirectory()
        if self.destination_directory:
            self.status_label.config(text=f"Selected Destination: {self.destination_directory}")

    def transfer_file(self):
        if not self.source_file:
            messagebox.showerror("Error", "Please select a file to transfer.")
            return
        
        if not self.destination_directory:
            messagebox.showerror("Error", "Please select a destination directory.")
            return
        
        try:
            shutil.copy(self.source_file, self.destination_directory)
            messagebox.showinfo("Success", f"File '{os.path.basename(self.source_file)}' transferred successfully.")
            self.status_label.config(text="")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to transfer file: {e}")

def file_transfers():
    root = tk.Tk()
    app = FileTransferApp()
    app.setup_gui(root)
    root.mainloop()

file_transfers()
