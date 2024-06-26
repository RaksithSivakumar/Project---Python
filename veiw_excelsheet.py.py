import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from pandastable import Table

class ExcelViewerApp:
    def __init_app__(self, root):
        self.master = root
        root.title("Excel Datasheet Viewer")
        root.geometry("800x600")
        root.configure(bg="#f0f0f0")

        self.label = tk.Label(root, text="Load and View Excel Datasheets", font=("Helvetica", 16), bg="#f0f0f0")
        self.label.pack(pady=20)

        self.upload_button = tk.Button(root, text="Upload Excel File", command=self.upload_excel, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
        self.upload_button.pack(pady=10)

        self.table_frame = tk.Frame(root)
        self.table_frame.pack(fill="both", expand=True)

    def upload_excel(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            self.load_excel(file_path)

    def load_excel(self, file_path):
        try:
            df = pd.read_excel(file_path)
            self.display_data(df)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load Excel file: {e}")

    def display_data(self, df):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        
        pt = Table(self.table_frame, dataframe=df, showtoolbar=True, showstatusbar=True)
        pt.show()

def create_excel_viewer_app():
    root = tk.Tk()
    app = ExcelViewerApp()
    app.__init_app__(root)
    root.mainloop()

create_excel_viewer_app()
