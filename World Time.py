import tkinter as tk
from tkinter import ttk
from time import strftime
import pytz
from datetime import datetime

class WorldClock(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("World Clock")
        self.geometry("400x200")
        self.configure(bg="lightblue")
        
        self.timezones = pytz.all_timezones
        
        self.create_widgets()
        self.update_time()

    def create_widgets(self):
        self.timezone_label = ttk.Label(self, text="Select Timezone:", font=("Helvetica", 12))
        self.timezone_label.pack(pady=10)
        
        self.timezone_combobox = ttk.Combobox(self, values=self.timezones, width=50)
        self.timezone_combobox.set("UTC")
        self.timezone_combobox.pack(pady=10)
        
        self.time_label = ttk.Label(self, text="", font=("Helvetica", 48), background="lightblue")
        self.time_label.pack(pady=20)
        
    def update_time(self):
        selected_timezone = self.timezone_combobox.get()
        timezone = pytz.timezone(selected_timezone)
        current_time = datetime.now(timezone).strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        
        self.after(1000, self.update_time)

if __name__ == "__main__":
    app = WorldClock()
    app.mainloop()
