import tkinter as tk
import ttkbootstrap as ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Hide Widgets')

def toggle_label():
    if label_visible.get():
        label.place_forget()
        label_visible.set(False)
    else:
        label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        label_visible.set(True)

button = ttk.Button(window, text = 'Toggle label', command=toggle_label)
button.place(x = 10, y = 10)

label_visible = tk.BooleanVar(value = True)
label = ttk.Label(window, text = 'Label')
label.place(relx = 0.5, rely = 0.5, anchor = 'center')

window.columnconfigure((0, 1, 2), weight = 1, uniform='a')
window.rowconfigure((0, 1), weight = 1, uniform='a')

def toggle_label_grid():
    if label_visible2.get():
        label2.grid_forget()
        label_visible2.set(False)
    else:
        label2.grid(column = 1, row = 1)
        label_visible2.set(True)
button2 = ttk.Button(window, text = 'Toggle label 2', command=toggle_label_grid)
button2.place(x = 200, y = 10)
label_visible2 = tk.BooleanVar(value = True)
label2 = ttk.Label(window, text = 'Label')

label2.grid(column = 1, row = 1)

pack_example = ttk.Frame(window)
pack_example.grid(column = 0, row = 1, sticky = 'nswe')

def toggle_label_pack():
    global label_visible3
    if label_visible3:
        label3.pack_forget()
        label_visible3 = False
        frame.pack(expand = True, before = button3)
    else:
        frame.pack_forget()
        label3.pack(expand=True, before = button3)
        label_visible3 = True

button3 = ttk.Button(pack_example, text = 'Toggle label 3', command=toggle_label_pack)

label_visible3 = True
frame = ttk.Frame(pack_example)
label3 = ttk.Label(pack_example, text = 'Label')
label3.pack(expand=True)

button3.pack()



window.mainloop()