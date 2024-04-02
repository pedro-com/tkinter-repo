'''
    grid:
        You create a grid with rows and columns, and set where each widget is by column and row.
        Grid only determines how much space a widget can occupy.
        You use sticky to determine how much space will be filled
        Can be weird when you have empty cells (tkinter tries to make the cells bigger if there is white space around them).
            Use uniform = 'a', for all the columns to be the same size
'''
import tkinter as tk
# from tkinter import ttk
from ttkbootstrap import ttk

window = tk.Tk()
window.title('Grid')
window.geometry('600x400')

label1 = ttk.Label(window, text = "Label 1", background = 'red')
label2 = ttk.Label(window, text = "Label 2", background = 'blue')
label3 = ttk.Label(window, text = "Label 3", background = 'green')
label4 = ttk.Label(window, text = "Label 4", background = 'yellow')
button1 = ttk.Button(window, text = 'Button 1')
button2 = ttk.Button(window, text = 'Button 2')
entry = ttk.Entry(window)

window.columnconfigure((0, 1, 2), weight = 1)
window.columnconfigure(3, weight = 10)

window.rowconfigure((0, 1, 2), weight = 1)
window.rowconfigure(3, weight = 3)


label1.grid(row = 0, column = 0, sticky = 'nsew')
label2.grid(row = 0, column = 1,rowspan = 3, sticky = 'nswe')

window.mainloop()