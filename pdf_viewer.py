import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import fitz

class PDFViewerApp:
    def setup(self, root):
        self.root = root
        self.root.title("PDF Viewer")
        self.root.geometry("800x600")
        self.root.configure(bg="#ECECEC")

        self.create_widgets()

    def create_widgets(self):
       
        self.control_frame = tk.Frame(self.root, bg="#ECECEC")
        self.control_frame.pack(pady=10)

        self.open_button = ttk.Button(self.control_frame, text="Open PDF", command=self.open_pdf)
        self.open_button.grid(row=0, column=0, padx=10)

        self.prev_button = ttk.Button(self.control_frame, text="Previous", command=self.prev_page)
        self.prev_button.grid(row=0, column=1, padx=10)

        self.next_button = ttk.Button(self.control_frame, text="Next", command=self.next_page)
        self.next_button.grid(row=0, column=2, padx=10)

        self.page_label = tk.Label(self.control_frame, text="Page 0/0", bg="#ECECEC")
        self.page_label.grid(row=0, column=3, padx=10)

        
        self.canvas = tk.Canvas(self.root, bg="#FFFFFF", width=600, height=800)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        self.pdf_document = None
        self.page_number = 0
        self.page_count = 0

    def open_pdf(self):
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            self.pdf_document = fitz.open(pdf_path)
            self.page_count = len(self.pdf_document)
            self.page_number = 0
            self.display_page()
        else:
            messagebox.showerror("Error", "No PDF file selected")

    def display_page(self):
        if self.pdf_document:
            page = self.pdf_document.load_page(self.page_number)
            pix = page.get_pixmap()

            
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            self.imgtk = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imgtk)

            self.page_label.config(text=f"Page {self.page_number + 1}/{self.page_count}")

    def next_page(self):
        if self.pdf_document and self.page_number < self.page_count - 1:
            self.page_number += 1
            self.display_page()

    def prev_page(self):
        if self.pdf_document and self.page_number > 0:
            self.page_number -= 1
            self.display_page()

root = tk.Tk()
app = PDFViewerApp()
app.setup(root)
root.mainloop()
