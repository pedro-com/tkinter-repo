import tkinter as tk
from tkinter import ttk
'''
Widgets can be updated with config
Label.config(text = 'some new text')
Label['text'] = 'some new text'
'''
def button_func():
    # Get content of the entry
    entry_text = entry.get()
    # Update the label
    # label.configure(text = 'some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'
    # print(label.configure()) to see all attributes

def reenable():
    label['text'] = 'some_text'
    entry['state'] = 'enable'

# Window
window = tk.Tk()
window.title('Getting and setting widgets')

# Widgets
# NOT all widgets have a get method
label = ttk.Label(master=window, text = "Some label")
label.pack()

# An entry has an state, which can be enabled or disabled
entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master=window, text='The button', command = button_func)
button.pack()

button_enable = ttk.Button(master=window, text='Reenable', command = reenable)
button_enable.pack()

window.mainloop()