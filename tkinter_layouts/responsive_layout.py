import tkinter as tk
import ttkbootstrap as ttk

class App(tk.Tk):
    def __init__(self, start_size):
        super().__init__()
        self.title('Responsive layout')
        self.geometry(f'{start_size}x{start_size}')
        self.frame = ttk.Frame(self)
        self.frame.pack(expand = True, fill = 'both')
        SizeNotifier(self, {300: self.create_small_layout, 600: self.create_medium_layout, 1200: self.create_large_layout})
        self.mainloop()

    def create_small_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        ttk.Label(self.frame, text = "Label 1", background = 'red').pack(expand = True, fill = 'both', padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label 2", background = 'green').pack(expand = True, fill = 'both', padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label 3", background = 'blue').pack(expand = True, fill = 'both', padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label 4", background = 'yellow').pack(expand = True, fill = 'both', padx = 10, pady = 10)
        self.frame.pack(expand = True, fill = 'both')

    def create_medium_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0, 1), weight = 1, uniform = 'a')
        self.frame.rowconfigure((0, 1), weight = 1, uniform = 'a')
        ttk.Label(self.frame, text = "Label 1", background = 'red').grid(row = 0, column = 0, sticky = 'sewn', padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label 2", background = 'green').grid(row = 0, column = 1, sticky = 'sewn', padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label 3", background = 'blue').grid(row = 1, column = 0, sticky = 'sewn', padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label 4", background = 'yellow').grid(row = 1, column = 1, sticky = 'sewn', padx = 10, pady = 10)
        self.frame.pack(expand = True, fill = 'both')

    def create_large_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        ttk.Label(self.frame, text = "Label 1", background = 'red').pack(side = 'left', expand = True, fill = 'both', padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label 2", background = 'green').pack(side = 'left',expand = True, fill = 'both', padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label 3", background = 'blue').pack(side = 'left',expand = True, fill = 'both', padx = 10, pady = 10)
        ttk.Label(self.frame, text = "Label 4", background = 'yellow').pack(side = 'left',expand = True, fill = 'both', padx = 10, pady = 10)
        self.frame.pack(expand = True, fill = 'both')

class SizeNotifier():
    def __init__(self, window, size_dictionary):
        self.window = window
        self.size_dict= {key: value for key, value in sorted(size_dictionary.items())}
        self.current_min_size = None
        self.window.bind('<Configure>', lambda event: self.check_size(event))
        self.window.update()

        min_width = list(self.size_dict)[0]
        min_height = self.window.winfo_height()
        self.window.minsize(min_width, min_height)
    
    def check_size(self, event):
        if not event.widget == self.window:
            return
        window_width = event.width
        checked_size = None
        for min_size in self.size_dict:
            delta = window_width - min_size
            if delta >= 0:
                checked_size = min_size
        if checked_size != self.current_min_size:
            self.current_min_size = checked_size
            self.size_dict[self.current_min_size]()

App(400)
            