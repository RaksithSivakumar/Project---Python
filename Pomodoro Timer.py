import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x250")
        self.root.resizable(False, False)

        self.work_time = 25 * 60  
        self.break_time = 5 * 60  
        self.current_time = self.work_time
        self.is_running = False
        self.is_break = False

        self.timer_label = tk.Label(self.root, text=self.format_time(self.current_time), font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=(20, 10))

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_timer)
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.update_timer()

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def update_timer(self):
        if self.is_running:
            self.current_time -= 1
            if self.current_time <= 0:
                if not self.is_break:
                    messagebox.showinfo("Pomodoro Timer", "Time for a break!")
                    self.current_time = self.break_time
                    self.is_break = True
                else:
                    messagebox.showinfo("Pomodoro Timer", "Back to work!")
                    self.current_time = self.work_time
                    self.is_break = False
                self.is_running = False
        self.timer_label.config(text=self.format_time(self.current_time))
        self.root.after(1000, self.update_timer)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True

    def pause_timer(self):
        if self.is_running:
            self.is_running = False

    def reset_timer(self):
        self.is_running = False
        self.current_time = self.work_time if not self.is_break else self.break_time
        self.timer_label.config(text=self.format_time(self.current_time))

root = tk.Tk()
app = PomodoroTimer(root)
root.mainloop()
