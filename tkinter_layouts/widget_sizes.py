'''
    tkinter uses most of the times the sizes passed in pack, place or grid.
    Widgets are also placed on top of other widgets when they are created
    label1.lift() or label1.lower() or .tkraise or .tklower, the argument aboveThis sets so that its above an specified widget.
'''
import tkinter as tk
import ttkbootstrap as ttk

window = tk.Tk()
window.geometry('400x300')

label1 = ttk.Label(window, text = 'Label 1', background='green')
label2 = ttk.Label(window, text = 'Label 2', background='red', width = 50)
button1 = ttk.Button(window, text = "Raise Label 1", command = lambda : label1.lift())
button2 = ttk.Button(window, text = "Raise Label 2", command = lambda : label2.lift())

# window.columnconfigure((0, 1), weight = 1, uniform = 'a')
# window.rowconfigure((0, 1), weight = 1, uniform = 'a')
# label1.grid(row = 0, column = 0)
# label2.grid(row = 0, column = 0, sticky = 'nsew')
# label1.lift() or label1.lower()
label1.place(x = 50, y = 100, width = 200, height = 150)
label2.place(x = 150, y = 60, width = 140, height = 100)

button1.place(rely = 1, relx = 0.8, anchor = 'se')
button2.place(rely = 1, relx = 1, anchor = 'se')

window.mainloop()