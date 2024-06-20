import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = tk.Tk()
root.title("Expense and Savings Tracker")
root.geometry("800x600")
root.configure(bg="#f0f0f0")


try:
    df = pd.read_csv("expenses.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Category", "Amount", "Date"])


def add_expense():
    category = category_entry.get().strip()
    amount_str = amount_entry.get().strip()
    date = date_entry.get().strip()

    if not category or not amount_str or not date:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    try:
        amount = float(amount_str)
    except ValueError:
        messagebox.showerror("Input Error", "Amount must be a number.")
        return
    
    global df
    df = df.append({"Category": category, "Amount": amount, "Date": date}, ignore_index=True)
    df.to_csv("expenses.csv", index=False)
    update_expense_list()
    messagebox.showinfo("Success", "Expense added successfully!")
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

def update_expense_list():
    for row in expense_list.get_children():
        expense_list.delete(row)
    
    for _, row in df.iterrows():
        expense_list.insert("", "end", values=(row["Category"], row["Amount"], row["Date"]))

def show_expense_chart():
    if df.empty:
        messagebox.showerror("No Data", "No expense data to plot.")
        return

    fig, ax = plt.subplots()
    df.groupby("Category")["Amount"].sum().plot(kind='bar', ax=ax)
    ax.set_title("Expenses by Category")
    ax.set_ylabel("Amount")
    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

category_label = tk.Label(root, text="Category:", font=("Helvetica", 12), bg="#f0f0f0")
category_label.pack(pady=5)
category_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
category_entry.pack(pady=5)

amount_label = tk.Label(root, text="Amount:", font=("Helvetica", 12), bg="#f0f0f0")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
amount_entry.pack(pady=5)

date_label = tk.Label(root, text="Date (YYYY-MM-DD):", font=("Helvetica", 12), bg="#f0f0f0")
date_label.pack(pady=5)
date_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
date_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Expense", command=add_expense, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
add_button.pack(pady=20)

show_chart_button = tk.Button(root, text="Show Expense Chart", command=show_expense_chart, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
show_chart_button.pack(pady=20)

expense_list = ttk.Treeview(root, columns=("Category", "Amount", "Date"), show="headings")
expense_list.heading("Category", text="Category")
expense_list.heading("Amount", text="Amount")
expense_list.heading("Date", text="Date")
expense_list.pack(pady=20)

update_expense_list()

root.mainloop()
