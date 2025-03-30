import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except:
            messagebox.showerror("Error", "Invalid Expression")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + button_text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('0', '1', '2', '/'),
    ('3', '4', '5', '*'),
    ('6', '7', '8', '-'),
    ('C', '9', '=', '+')
]

for r, row in enumerate(buttons, start=1):
    for c, text in enumerate(row):
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: on_click(t)).grid(row=r, column=c)

root.mainloop()
