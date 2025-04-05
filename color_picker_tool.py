import tkinter as tk
from tkinter import colorchooser

# Function to open the color picker dialog and update the label and canvas
def pick_color():
    # Open the color chooser dialog and get the selected color
    color_code = colorchooser.askcolor(title="Choose a color")[1]
    
    # Update the label with the color code
    color_label.config(text=f"Selected Color: {color_code}", bg=color_code)
    
    # Update the canvas background with the selected color
    color_canvas.config(bg=color_code)

# Create the main window
root = tk.Tk()
root.title("Color Picker Tool")
root.geometry("400x300")

# Create a label to display the selected color code
color_label = tk.Label(root, text="Selected Color: None", font=("Arial", 16))
color_label.pack(pady=20)

# Create a canvas to display the selected color
color_canvas = tk.Canvas(root, width=200, height=100, bg="white")
color_canvas.pack(pady=20)

# Create a button to open the color picker dialog
pick_color_button = tk.Button(root, text="Pick a Color", command=pick_color, font=("Arial", 16))
pick_color_button.pack(pady=20)

# Start the main loop
root.mainloop()
