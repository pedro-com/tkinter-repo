'''
    pack:
        Packs widgets horizontally
    grid:
        Creates a grid over the window and you use it to place widgets over it
    place:
        Places the widget
'''
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Layout intro')
window.geometry('600x400')

label1 = tk.Label(window, text = 'Label 1', background='red')
label2 = tk.Label(window, text = 'Label 2', background='blue')

# label1.pack(side = 'left', expand = True, fill = 'both')
# label2.pack(side = 'left', expand = True, fill = 'both')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

label1.grid(row = 0, column = 1, sticky= 'nsew')
label2.grid(row = 1, column = 2, sticky= 'nsew')

label1.place(x = 100, y = 200, width = 200, height = 100)
label2.place(relx = 0.5, rely = 0.5, relwidth = 1, anchor = 'center')
window.mainloop()