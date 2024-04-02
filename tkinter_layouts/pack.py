'''
    pack:
        side: left, right, top, bottom 
        expand: vertical or horizontal space a widget can occupy
        fill: sets how much space the widget will occupy
        padx or pady: Creates padding around the widget
        ipadx or ipady: Expands the widget
    Can combine sides, but it depends on the order.
    You should pack things only in one direction, but use Frames to sort them how you want. 
'''
import tkinter as tk
# from tkinter import ttk
from ttkbootstrap import ttk
window = tk.Tk()
window.title('Pack')
window.geometry('600x500')
label1 = ttk.Label(window, text="Label 1", background='red')
label2 = ttk.Label(window, text="Label 2", background="green")
label3 = ttk.Label(window, text="Label 3", background="blue")
button = ttk.Button(window, text="Button")

label1.pack(fill='x')
label2.pack(expand = True)
label3.pack(expand = True, fill='both')
button.pack(fill='x')

window.mainloop()

