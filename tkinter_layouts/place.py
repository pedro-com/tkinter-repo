'''
    place:
        Widgets can be placed by specifying the left, top, width and height of the Widget.
        (left, top) is the left corner of the widget.
        You can place it with an absolute position [0, window_size] or a relative position to the window [0, 1].
        You can also set the anchor, which is the position of the (x, y) point.
            - center, in the center of the widget
'''
import tkinter as tk
import ttkbootstrap as ttk
# from tkinter import ttk

window = tk.Tk()
window.title('Place')
window.geometry('400x600')

label1 = ttk.Label(window, text = "Label 1", background = 'red')
label2 = ttk.Label(window, text = "Label 2", background = 'blue')
label3 = ttk.Label(window, text = "Label 3", background = 'green')
button = ttk.Button(window, text = "Button")

label1.place(x = 300, y = 100, width = 100, height = 200)
label2.place(relx = 0.2, rely = 0.1, relwidth=0.4, relheight = 0.5)
label3.place(x = 80, y = 60, width = 160, height = 300)
button.place(relx = 1, rely = 1)

frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text = "Label 2", background = 'yellow')
frame_button = ttk.Button(frame, text = "Button")

frame.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 1)
frame_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.5)
frame_button.place(relx = 0, rely = 0.5, relwidth = 1, relheight = 0.5)

ex_button = ttk.Button(window, text = "Button")
ex_button.place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth=0.5, relheight=0.5)


window.mainloop()