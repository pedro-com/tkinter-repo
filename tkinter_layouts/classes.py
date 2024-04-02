'''
    Use a tkinter widget via classes to organize the code with inheritance
'''
import tkinter as tk
import ttkbootstrap as ttk

class App(tk.Tk):
    def __init__(self, name:str, size):
        # Main setup
        super().__init__()
        self.title(name)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        # Widgets
        self.menu = Menu(self)
        self.main = Main(self)

        # Run
        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth=0.3, relheight = 1)
        self.columnconfigure((0, 1, 2), weight = 1, uniform = 'a')
        self.rowconfigure((0, 1, 2, 3, 4), weight = 1, uniform = 'a')
        self.create_widgets()

    def create_widgets(self):
        menu_button1 = ttk.Button(self, text = 'Button 1')
        menu_button2 = ttk.Button(self, text = 'Button 2')
        menu_button3 = ttk.Button(self, text = 'Button 3')

        menu_slider1 = ttk.Scale(self, orient = 'vertical')
        menu_slider2 = ttk.Scale(self, orient = 'vertical')

        toggle_frame = ttk.Frame(self)
        menu_toggle1 = ttk.Checkbutton(toggle_frame, text = "Check 1")
        menu_toggle2 = ttk.Checkbutton(toggle_frame, text = "Check 2")

        menu_button1.grid(row = 0, column = 0, columnspan=2, sticky = 'nsew')
        menu_button2.grid(row = 0, column = 2, columnspan=2, sticky = 'nsew')
        menu_button3.grid(row = 1, column = 0, columnspan=3, sticky = 'nsew')

        menu_slider1.grid(row = 2, column = 0, pady = 20, sticky = 'nsew', rowspan = 2)
        menu_slider2.grid(row = 2, column = 2, pady = 20, sticky = 'nsew', rowspan = 2)

        toggle_frame.grid(row = 4, column = 0, columnspan = 3, sticky = 'nsew')
        menu_toggle1.pack(side = 'left', expand = True)
        menu_toggle2.pack(side = 'left', expand = True)

class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, y = 0, relwidth = 0.7, relheight = 1)
        self.entry1 = Entry(self, 'red', 'Label 1', 'Button 1')
        self.entry2 = Entry(self, 'green', 'Label 2', 'Button 2')

class Entry(ttk.Frame):
    def __init__(self, parent, color, label_text, button_text):
        super().__init__(parent)
        self.pack(side = 'left', fill = 'both', expand = 'True', padx = 20, pady = 20)
        label = ttk.Label(self, text = label_text, background = color)
        button = ttk.Button(self, text = button_text)
        label.pack(fill = 'both', expand = 'True')
        button.pack(fill = 'both', expand = 'True', pady = 10)

App('Class based app', (600, 600))