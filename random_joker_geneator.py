import requests
import tkinter as tk
from tkinter import messagebox

def fetch_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}", None
    except requests.RequestException as e:
        return None, f"An error occurred: {e}"

def show_joke():
    joke, error = fetch_random_joke()
    if joke:
        joke_label.config(text=joke)
    else:
        messagebox.showerror("Error", error)

root = tk.Tk()
root.title("Random Joke Generator")
root.geometry("500x300")
root.configure(bg="#ffefd5")

joke_label = tk.Label(root, text="Click the button to get a random joke!", wraplength=400, justify="center", font=("Helvetica", 14), bg="#ffefd5", fg="#333333")
joke_label.pack(pady=30)

joke_button = tk.Button(root, text="Get Joke", command=show_joke, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", activebackground="#45a049", padx=20, pady=10)
joke_button.pack(pady=20)

footer_label = tk.Label(root, text="Enjoy your jokes! 😊", font=("Helvetica", 10, "italic"), bg="#ffefd5", fg="#555555")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
