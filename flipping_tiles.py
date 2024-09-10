import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Flipping Tiles - Memory Game")
root.geometry("500x600")
root.config(bg="#F0F8FF")

num_pairs = 8 
values = list(range(1, num_pairs + 1)) * 2  
random.shuffle(values)  

buttons = []  
flipped_tiles = []  
matched_pairs = []  
moves = 0  

def flip_tile(i):
    global moves
    if i in flipped_tiles or i in matched_pairs:
        return
    
    buttons[i].config(text=values[i], bg="#FFD700", fg="black", state="disabled")
    flipped_tiles.append(i)
    
    if len(flipped_tiles) == 2:
        root.after(500, check_match)
        moves += 1
        move_label.config(text=f"Moves: {moves}")

def check_match():
    if values[flipped_tiles[0]] == values[flipped_tiles[1]]:
        for i in flipped_tiles:
            buttons[i].config(bg="#32CD32")  
        matched_pairs.extend(flipped_tiles)
    else:
        for i in flipped_tiles:
            buttons[i].config(text="", bg="#ADD8E6", state="normal")
    
    flipped_tiles.clear()
    
    if len(matched_pairs) == len(values):
        messagebox.showinfo("Congratulations!", f"You matched all the tiles in {moves} moves!")

def create_buttons():
    for i in range(len(values)):
        btn = tk.Button(root, text="", width=10, height=4, bg="#ADD8E6", 
                        font=("Helvetica", 12, "bold"),
                        command=lambda i=i: flip_tile(i))
        btn.grid(row=i // 4, column=i % 4, padx=10, pady=10)
        buttons.append(btn)

move_label = tk.Label(root, text="Moves: 0", font=("Helvetica", 16, "bold"), bg="#F0F8FF")
move_label.grid(row=num_pairs // 4, column=0, columnspan=4, pady=20)

create_buttons()

root.mainloop()
