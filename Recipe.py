import tkinter as tk
from tkinter import simpledialog, messagebox

recipes = {}

def add_recipe():
    name = simpledialog.askstring("Recipe Name", "Enter the recipe name:")
    ingredients = simpledialog.askstring("Ingredients", "Enter the ingredients (comma-separated):")
    instructions = simpledialog.askstring("Instructions", "Enter the instructions:")
    if name and ingredients and instructions:
        recipes[name] = {"ingredients": ingredients, "instructions": instructions}
        update_recipe_list()

def view_recipe():
    selected_recipe = recipe_listbox.get(tk.ACTIVE)
    if selected_recipe:
        recipe = recipes[selected_recipe]
        messagebox.showinfo(selected_recipe, f"Ingredients:\n{recipe['ingredients']}\n\nInstructions:\n{recipe['instructions']}")

def update_recipe_list():
    recipe_listbox.delete(0, tk.END)
    for recipe in recipes:
        recipe_listbox.insert(tk.END, recipe)

root = tk.Tk()
root.title("Recipe Book")
root.geometry("400x300")

tk.Button(root, text="Add Recipe", command=add_recipe).pack(pady=10)
tk.Button(root, text="View Recipe", command=view_recipe).pack(pady=10)
recipe_listbox = tk.Listbox(root)
recipe_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
