'''
    styles:
        Inbuilt styling tools (widget options and the style object).
        External themes
        External modules
    Google colour picker
'''
import tkinter as tk
from tkinter import ttk, font

window = tk.Tk()
window.title('Styling')
window.geometry('400x400')
style = ttk.Style()
print(style.theme_names())
style.theme_use('clam')

# TButton for all the buttons
style.configure('new.TButton', background='green')
style.map("new.TButton", foreground = [('pressed', "red"), ("disabled", "yellow")])
print(font.families())
label = ttk.Label(window,
                  text = "Label",
                  background = "red",
                  foreground = "white",
                  font = ("Jokeman", 24),
                  justify="right")

label.pack()

label2 = ttk.Label(window, background = '#08F').pack()

button = ttk.Button(window, text = "Button", style = "new.TButton").pack()

window.mainloop()