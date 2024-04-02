import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Menu')

menu = tk.Menu(window)
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label = "New", command = lambda: print("Open file"))
file_menu.add_separator()
file_menu.add_command(label = "Old", command = lambda: print("Close file"))

menu.add_cascade(label = 'File', menu = file_menu)
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label = "Help entry", command = lambda : print("Help"))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = "check", onvalue = "on", offvalue = "off", variable= help_check_string)

menu.add_cascade(label = "Help", menu = help_menu)
window.configure(menu = menu)

window.mainloop()