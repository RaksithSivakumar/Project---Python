import customtkinter as ctk
from tkinter import messagebox
import datetime

app = ctk.CTk()
app.title('Expense Tracker')
app.geometry('600x500')
app.configure(fg_color='#020a24')

font1 = ('Arial', 20, 'bold')
font2 = ('Arial', 15, 'bold')
font3 = ('Arial', 12)

# Sample data store
expenses = []

def add_expense():
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid amount")
        return
    
    category = category_combo.get()
    description = description_entry.get()
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    expenses.append({'amount': amount, 'category': category, 'description': description, 'date': date})
    messagebox.showinfo("Success", "Expense added successfully")
    amount_entry.delete(0, 'end')
    description_entry.delete(0, 'end')

def view_expenses():
    expenses_window = ctk.CTkToplevel(app)
    expenses_window.title("Expenses")
    expenses_window.geometry("600x400")
    
    text_area = ctk.CTkTextbox(expenses_window, width=550, height=350)
    text_area.pack(pady=10)
    
    text = "Date\t\tAmount\tCategory\tDescription\n"
    text += "-"*80 + "\n"
    for expense in expenses:
        text += f"{expense['date']}\t{expense['amount']}\t{expense['category']}\t{expense['description']}\n"
    
    text_area.insert('1.0', text)
    text_area.configure(state='disabled')

def view_reports():
    report_window = ctk.CTkToplevel(app)
    report_window.title("Expense Reports")
    report_window.geometry("400x300")
    
    total_amount = sum(expense['amount'] for expense in expenses)
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += expense['amount']
    
    text_area = ctk.CTkTextbox(report_window, width=350, height=250)
    text_area.pack(pady=10)
    
    text = f"Total Expenses: {total_amount}\n\n"
    for category, total in category_totals.items():
        text += f"{category}: {total}\n"
    
    text_area.insert('1.0', text)
    text_area.configure(state='disabled')

# Widgets
amount_label = ctk.CTkLabel(app, text="Amount:", font=font2, fg_color='#020a24')
amount_label.pack(pady=10)

amount_entry = ctk.CTkEntry(app, font=font3)
amount_entry.pack(pady=10)

category_label = ctk.CTkLabel(app, text="Category:", font=font2, fg_color='#020a24')
category_label.pack(pady=10)

category_combo = ctk.CTkComboBox(app, values=["Food", "Transport", "Utilities", "Entertainment", "Other"], font=font3)
category_combo.pack(pady=10)
category_combo.set("Food")

description_label = ctk.CTkLabel(app, text="Description:", font=font2, fg_color='#020a24')
description_label.pack(pady=10)

description_entry = ctk.CTkEntry(app, font=font3)
description_entry.pack(pady=10)

add_button = ctk.CTkButton(app, text="Add Expense", font=font2, command=add_expense)
add_button.pack(pady=10)

view_button = ctk.CTkButton(app, text="View Expenses", font=font2, command=view_expenses)
view_button.pack(pady=10)

report_button = ctk.CTkButton(app, text="View Reports", font=font2, command=view_reports)
report_button.pack(pady=10)

app.mainloop()
