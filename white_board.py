import tkinter as tk
from tkinter.colorchooser import askcolor

class DigitalWhiteboard:
    def whiteboard(self, root):
        self.root = root
        self.root.title("Digital Whiteboard")
        self.root.geometry("800x600")
        
        self.current_color = 'black'
        self.brush_size = 5
        
        self.canvas = tk.Canvas(self.root, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.canvas.bind('<B1-Motion>', self.paint)
        
        
        self.create_buttons()
        
    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg='lightgrey')
        button_frame.pack(fill=tk.X)
        
        color_button = tk.Button(button_frame, text='Color', command=self.choose_color)
        color_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        clear_button = tk.Button(button_frame, text='Clear', command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        decrease_brush_button = tk.Button(button_frame, text='-', command=self.decrease_brush_size)
        decrease_brush_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        increase_brush_button = tk.Button(button_frame, text='+', command=self.increase_brush_size)
        increase_brush_button.pack(side=tk.LEFT, padx=5, pady=5)
        
    def choose_color(self):
        color = askcolor()[1]
        if color:
            self.current_color = color
            
    def clear_canvas(self):
        self.canvas.delete('all')
        
    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.current_color, outline=self.current_color)
        
    def decrease_brush_size(self):
        if self.brush_size > 1:
            self.brush_size -= 1
            
    def increase_brush_size(self):
        self.brush_size += 1


def white_board():
    root = tk.Tk()
    app = DigitalWhiteboard()
    app.whiteboard(root)
    root.mainloop()

white_board()

