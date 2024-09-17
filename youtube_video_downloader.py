from tkinter import *
from tkinter import messagebox
from pytube import YouTube

# Function to download video
def download_video():
    try:
        url = url_entry.get()  # Get URL from the entry field
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()  # Get highest resolution stream
        stream.download()  # Download the video
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {str(e)}")

# Initialize the tkinter window
root = Tk()
root.title("YouTube Video Downloader")
root.geometry("400x200")

# URL label
url_label = Label(root, text="Enter YouTube URL:", font=("Arial", 12))
url_label.pack(pady=10)

# URL entry
url_entry = Entry(root, width=50, font=("Arial", 12))
url_entry.pack(pady=5)

# Download button
download_button = Button(root, text="Download", command=download_video, font=("Arial", 12), bg="green", fg="white")
download_button.pack(pady=20)

# Start the tkinter main loop
root.mainloop()
