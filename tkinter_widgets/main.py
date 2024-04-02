'''
Widgets are the building blocks of tkinters.
    - Widgets is a text a button a checkbox a menu a frame...

Two set of widgets:
- Tk Widgets
- Ttk widgets (more modern)

https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
'''
import tkinter as tk
from tkinter import ttk
from random import choice

def button_func():
    print('Button was pressed')

# Create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x700')

# Create widgets
# Label
label = ttk.Label(master=window, text='Testing text')
label.pack()

# Text box
text_box = tk.Text(master = window)
# By default packs it at the middle and top of the window
text_box.pack()

# Entry
entry = ttk.Entry(master=window)
entry.pack()


my_label = ttk.Label(master=window, text='My label')
my_label.pack()
my_button = ttk.Button(master = window, text ='Say hello', command = lambda :print('hello'))
my_button.pack()

# Button
button = ttk.Button(master = window, text ='Button text', command = button_func)
button.pack()

# Combobox
items = ('Ice Cream', 'Sandwitch', 'Pizza')
food_str = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable= food_str)
combo['values'] = items
# combo.configure(values = items)
combo.pack()

combo.bind('<<ComboboxSelected>>', lambda event: combo_label.configure(text = f'Selected value: {food_str.get()}'))

combo_label = ttk.Label(window, text = 'a label')
combo_label.pack()

# SpinBox
spin_int = tk.IntVar()
spin = ttk.Spinbox(window,
    from_=3,
    to=20,
    increment = 3,
    command=lambda: print('Arrow pressed'),
    textvariable=spin_int
)
spin.bind('<<Increment>>', lambda event: print('up '))
spin.bind('<<Decrement>>', lambda event: print('down'))
spin.pack()

letters = ('A', 'B', 'C', 'D', 'E')
spin_str = tk.StringVar(value = 'A')
ex_spin = ttk.Spinbox(window, textvariable=spin_str, values = letters)
ex_spin.bind('<<Decrement>>', lambda event: print(spin_str.get()))
ex_spin.pack()

# Canvas
canvas = tk.Canvas(window, bg='white')
canvas.pack()

# left, top, right, bottom, P = (left, top), U = (left + right, top), V = (left + right. top - down)
# canvas.create_rectangle((50, 20, 100, 200), fill='red', width=10, dash = (1, 2), outline = 'green')
# canvas.create_line((0, 0, 100, 150), fill='blue')
# canvas.create_oval(0, 0, 100, 300, fill='green')
# canvas.create_polygon((0, 0, 100, 200, 300, 50))
# canvas.create_arc((200, 0, 300, 100), start = 45, style = tk.ARC)
# canvas.create_text((0, 0), text = 'this is some text')

# canvas.create_window((50, 100), window = ttk.Label(window, text= 'This is a text in a canvas'))
def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval(x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2)

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 1
    else:
        brush_size -= 1
    brush_size = max(0, min(brush_size, 50))

brush_size = 4
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)

# Tree view
table = ttk.Treeview(window, columns = ('first', 'last', 'email'), show = 'headings')
table.heading('first', text = 'First name')
table.heading('last', text = 'Last name')
table.heading('email', text = 'Email')
# index = tk.END
table.insert(parent = '', index = 0, values = ('John', 'Doe', 'JohnDow@email.com'))

def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def item_delete(_):
    for i in table.selection():
        table.delete(i)

table.bind('<<TreeviewSelect>>', lambda event: item_select)
table.bind('<<Delete>>', item_delete)
# Run
# Mainloop updates the GUI and checks for events
window.mainloop()
# Does not execute until the window is closed
print('hello')