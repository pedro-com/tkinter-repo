import tkinter as tk
import ttkbootstrap as ttk 
from tkinter import messagebox
'''
    tkinter message box
    https://docs.python.org/3/library/tkinter.messagebox.html
'''
window = tk.Tk()
window.geometry('600x400')
window.title('Multiple windows')

class Extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Extra window")
        self.geometry("200x200")
        ttk.Label(self, text = "Label").pack()
        ttk.Button(self, text = "Button").pack()

def ask_yes_no():
    answer = messagebox.askquestion('Title', 'Body')
    print(answer)

def show_info():
    messagebox.showinfo('Show info')

def create_window():
    global extra_window
    extra_window = Extra()
    '''
    extra_window = tk.Toplevel()
    extra_window.title("Extra window")
    extra_window.geometry("200x200")
    ttk.Label(extra_window, text = "Label").pack()'''

def close_window():
    extra_window.destroy()

button1 = ttk.Button(window, text = "Open main window", command = create_window)
button1.pack(expand = True)
button2 = ttk.Button(window, text = "Close main window", command = close_window)
button2.pack(expand = True)

button3 = ttk.Button(window, text = "Create yes/no window", command = ask_yes_no)
button3.pack(expand = True)

button4 = ttk.Button(window, text = "Create info window", command = show_info)
button4.pack(expand = True)

window.mainloop()