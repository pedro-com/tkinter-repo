'''
    ttk.Frame is just an empty widget to place other widgets within it.
'''
import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.geometry('600x400')
window.title('Frames and parenting')

frame = ttk.Frame(window, width = 100, height = 200, borderwidth = 10, relief = tk.GROOVE)
# Sets the size as the frames and not as the children
frame.pack_propagate(False)
frame.pack(side = 'left')

# TTk 
label = ttk.Label(frame, text = 'Label in frame')
label.pack()

button = ttk.Button(frame, text = 'Button')
button.pack()

label2 = ttk.Label(window, text ='Label outside of frame')
label2.pack(side = 'left')

frame2 = ttk.Frame(window, width = 100, height = 200, borderwidth = 10, relief = tk.GROOVE)
# Sets the size as the frames and not as the children
frame2.pack(side = 'right')

# TTk 
label2 = ttk.Label(frame2, text = 'Label in frame')
label2.pack()

button2 = ttk.Button(frame2, text = 'Button in frame')
button2.pack()

window.mainloop()