'''
    Classes:
        You inherit from a widget and add custom parts.
        This can create complex layouts.
        Can also end up creating lots of classes.
    Functional:
        Create a widget in a function and return it.
        Easier to organise when you create smaller components
'''
import tkinter as tk
import ttkbootstrap as ttk

def segment(parent, label_text, button_text):
    frame = ttk.Frame(parent)
    frame.rowconfigure(0, weight = 1, uniform = 'a')
    frame.columnconfigure((0, 1, 2), weight = 1, uniform = 'a')
    ttk.Label(frame, text = label_text).grid(row = 0, column = 0)
    ttk.Button(frame, text = button_text).grid(row = 0, column = 1)
    return frame

class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(master = parent)
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.columnconfigure((0, 1, 2), weight = 1, uniform = 'a')
        ttk.Label(self, text = label_text).grid(row = 0, column = 0)
        ttk.Button(self, text = button_text).grid(row = 0, column = 1)
        self.create_fill().grid(row = 0, column = 2, sticky = 'nswe')
        self.pack(expand = True, fill = 'both')

    def create_fill(self):
        frame = ttk.Frame(self)
        ttk.Entry(frame).pack(expand = True, fill = 'both')
        ttk.Button(frame, text = 'Exercise').pack(expand = True, fill = 'both')
        return frame

window = tk.Tk()
window.title('Widgets and return')
window.geometry('400x600')

Segment(window, 'label', 'button')
Segment(window, 'label', 'button')
Segment(window, 'label', 'button')
Segment(window, 'label', 'button')
Segment(window, 'label', 'button')
Segment(window, 'label', 'button')
segment(window, 'label_func', 'button_func').pack(expand = True, fill = 'both')

window.mainloop()