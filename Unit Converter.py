import customtkinter as ctk
from tkinter import messagebox

app = ctk.CTk()
app.title('Unit Converter')
app.geometry('500x450')
app.configure(fg_color='#020a24')

font1 = ('Arial', 30, 'bold')
font2 = ('Arial', 25, 'bold')
font3 = ('Arial', 15, 'bold')

def update_units(event=None):
    unit_type = unit_type_combo.get()
    if unit_type == "Length":
        units = ["meters", "kilometers", "miles", "feet"]
    elif unit_type == "Weight":
        units = ["grams", "kilograms", "pounds", "ounces"]
    elif unit_type == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]

    from_unit_combo.configure(values=units)
    to_unit_combo.configure(values=units)
    from_unit_combo.set(units[0])
    to_unit_combo.set(units[1])

def convert():
    unit_type = unit_type_combo.get()
    from_unit = from_unit_combo.get()
    to_unit = to_unit_combo.get()
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")
        return

    if unit_type == "Length":
        result = convert_length(amount, from_unit, to_unit)
    elif unit_type == "Weight":
        result = convert_weight(amount, from_unit, to_unit)
    elif unit_type == "Temperature":
        result = convert_temperature(amount, from_unit, to_unit)
    
    result_label.configure(text=f"Result: {result} {to_unit}")

def convert_length(amount, from_unit, to_unit):
    
    conversions = {
        "meters": 1,
        "kilometers": 1000,
        "miles": 1609.34,
        "feet": 0.3048
    }
    return amount * conversions[from_unit] / conversions[to_unit]

def convert_weight(amount, from_unit, to_unit):
    
    conversions = {
        "grams": 1,
        "kilograms": 1000,
        "pounds": 453.592,
        "ounces": 28.3495
    }
    return amount * conversions[from_unit] / conversions[to_unit]

def convert_temperature(amount, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return amount * 9/5 + 32
        elif to_unit == "Kelvin":
            return amount + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (amount - 32) * 5/9
        elif to_unit == "Kelvin":
            return (amount - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return amount - 273.15
        elif to_unit == "Fahrenheit":
            return (amount - 273.15) * 9/5 + 32

    return amount


unit_type_label = ctk.CTkLabel(app, text="Unit Type:", font=font2, fg_color='#020a24')
unit_type_label.pack(pady=10)

unit_type_combo = ctk.CTkComboBox(app, values=["Length", "Weight", "Temperature"], font=font3)
unit_type_combo.pack(pady=10)
unit_type_combo.bind("<<ComboboxSelected>>", update_units)
unit_type_combo.set("Length")

from_unit_label = ctk.CTkLabel(app, text="From Unit:", font=font2, fg_color='#020a24')
from_unit_label.pack(pady=10)

from_unit_combo = ctk.CTkComboBox(app, font=font3)
from_unit_combo.pack(pady=10)

to_unit_label = ctk.CTkLabel(app, text="To Unit:", font=font2, fg_color='#020a24')
to_unit_label.pack(pady=10)

to_unit_combo = ctk.CTkComboBox(app, font=font3)
to_unit_combo.pack(pady=10)

amount_label = ctk.CTkLabel(app, text="Amount:", font=font2, fg_color='#020a24')
amount_label.pack(pady=10)

amount_entry = ctk.CTkEntry(app, font=font3)
amount_entry.pack(pady=10)

convert_button = ctk.CTkButton(app, text="Convert", font=font3, command=convert)
convert_button.pack(pady=20)

result_label = ctk.CTkLabel(app, text="", font=font2, fg_color='#020a24')
result_label.pack(pady=10)


update_units()

app.mainloop()
