import textile
import tkinter as tk

def ConvertToHtml():
    inp = T.get(1.0, "end-1c")
    html = textile.textile(inp)
    print("\nAfter converted to HTML: \n", html)
    lbl.config(text="Converted Html: " + html)

root = tk.Tk()
root.geometry("500x300")  
root.configure(bg='#2c3e50')  

T = tk.Text(root, height=10, width=60, bg='#ecf0f1', fg='#2c3e50', font=('Arial', 12))
T.pack(pady=10)
T.insert(tk.END, "")

b1 = tk.Button(root, text="Submit", command=ConvertToHtml, bg='#3498db', fg='#ecf0f1', font=('Arial', 12))
b1.pack(pady=5)

lbl = tk.Label(root, text="", wraplength=450, justify="left", bg='#2c3e50', fg='#ecf0f1', font=('Arial', 12))
lbl.pack(pady=10)

root.mainloop()
