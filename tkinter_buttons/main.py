'''
    Tkinter buttons:
        - Button
        - Checkbutton
        - Radiobutton
'''
import tkinter as tk
from tkinter import ttk

# Setup
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

# Button string
button_string = tk.StringVar(value = 'The button')
# Button
button = tk.Button(master = window, text = 'A simple button', command = lambda: print('This button'), textvariable=button_string)
button.pack()

# Checkbutton
# check_var = tk.StringVar()
check_var = tk.IntVar()
# check_var = tk.BooleanVar()
check = ttk.Checkbutton(window, text = 'checkbox1', command = lambda: print(check_var.get()), variable = check_var, onvalue=10, offvalue=5)
check.pack()

# Radio button
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text='Radiobutton1',
    value='radio_1',
    variable = radio_var,
    command = lambda: print(radio_var.get())
)
radio1.pack()

radio2 = ttk.Radiobutton(window, text='Radiobutton1', value = 2, variable = radio_var)
radio2.pack()

# Exercise
def uncheck():
    bool_var.set(False)

bool_var = tk.BooleanVar()
radio_var2 = tk.StringVar()

check_ex = tk.Checkbutton(window,
    text='Ex check box',
    variable=bool_var,
    command = lambda: print(radio_var2.get()),
    onvalue = True,
    offvalue = False
)
check_ex.pack()

radio3 = ttk.Radiobutton(window,
    text = 'Radio A',
    value='A',
    command=uncheck,
    variable = radio_var2
)
radio3.pack()

radio4 = ttk.Radiobutton(window,
    text = 'Radio B',
    value='B',
    command=uncheck,
    variable = radio_var2
)
radio4.pack()
# Run
window.mainloop()