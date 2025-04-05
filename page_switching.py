import tkinter as tk
from tkinter import ttk

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Tkinter Page Switcher")
        self.geometry("400x300")
        
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(StartPage)
    
    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = ttk.Label(self, text="Start Page", font=("Arial", 18))
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Go to Page One", command=lambda: controller.show_frame(PageOne))
        button1.pack()
        
        button2 = ttk.Button(self, text="Go to Page Two", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = ttk.Label(self, text="Page One", font=("Arial", 18))
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(self, text="Back to Start Page", command=lambda: controller.show_frame(StartPage))
        button.pack()
        
        button2 = ttk.Button(self, text="Go to Page Two", command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = ttk.Label(self, text="Page Two", font=("Arial", 18))
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(self, text="Back to Start Page", command=lambda: controller.show_frame(StartPage))
        button.pack()
        
        button2 = ttk.Button(self, text="Go to Page One", command=lambda: controller.show_frame(PageOne))
        button2.pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
