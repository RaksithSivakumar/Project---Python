import tkinter as tk
from tkinter import messagebox
import pyautogui
import cv2
import numpy as np
from PIL import ImageGrab

class ScreenRecorder:
    def initialize(self, root):
        self.root = root
        self.root.title("Screen Recorder")
        self.root.geometry("300x150")
        self.root.configure(bg="#ececec")

        self.is_recording = False

        self.start_button = tk.Button(root, text="Start Recording", command=self.start_recording, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Recording", command=self.stop_recording, font=("Helvetica", 12), bg="#f44336", fg="white", state=tk.DISABLED)
        self.stop_button.pack(pady=10)

    def start_recording(self):
        self.is_recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.record_screen()

    def stop_recording(self):
        self.is_recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        messagebox.showinfo("Info", "Recording stopped and saved as output.avi")

    def record_screen(self):
        screen_size = (pyautogui.size().width, pyautogui.size().height)
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter("output.avi", fourcc, 20.0, screen_size)

        while self.is_recording:
            img = ImageGrab.grab(bbox=(0, 0, screen_size[0], screen_size[1]))
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            out.write(frame)
            self.root.update()

        out.release()

root = tk.Tk()
app = ScreenRecorder()
app.initialize(root)
root.mainloop()
