import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('Button was pressed')

# Window
window = tk.Tk()
window.title('Tkinter variables')

# Tkinter variables
string_var = tk.StringVar(value='Test')
# Widgets
label = ttk.Label(master=window, text = 'Label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable=string_var)
entry.pack()

entry2 = ttk.Entry(master = window, textvariable=string_var)
entry2.pack()

# Run
window.mainloop()