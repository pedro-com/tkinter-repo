import tkinter as tk
import ttkbootstrap as ttk

class ListFrame(ttk.Frame):
    def __init__(self, parent, num_items, item_height):
        super().__init__(master = parent)
        self.pack(expand = True, fill = 'both')
        self.num_items = num_items
        self.list_height = self.num_items * item_height

        self.canvas = tk.Canvas(self, background = 'red', scrollregion=(0, 0, self.winfo_width(), 1000))
        self.canvas.pack(expand = True, fill = 'both')
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta), "units"))

        self.scrollbar = ttk.Scrollbar(self, orient = 'vertical', command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')
        
        self.frame = ttk.Frame(self)
        for idx in range(self.num_items):
            self.create_item(idx).pack(expand = True, fill = 'both', pady = 4, padx = 10)
        self.bind('<Configure>', self.update_size)
    
    def update_size(self, event):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta), "units"))
        else:
            height = self.winfo_height()
            self.canvas.unbind_all('<Mousewheel>')

        self.canvas.create_window(
            (0, 0),
            window = self.frame,
            anchor = 'nw',
            width = self.winfo_width(),
            height = height
        )

    def create_item(self, idx):
        frame = ttk.Frame(self.frame)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0, 1, 2), weight = 1)
        ttk.Label(frame, text = f'Label 1.{idx}').grid(row = 0, column = 0, sticky = 'nswe')
        ttk.Label(frame, text = f'Label 2.{idx}').grid(row = 0, column = 1, sticky = 'nswe')
        ttk.Button(frame, text = f'Button {idx}').grid(row = 0, column = 2, rowspan = 3, sticky = 'nswe')
        return frame


window = tk.Tk()
window.geometry('500x500')
window.title('Scrolling')

list_frame = ListFrame(window, 100, 50)

window.mainloop()