import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
# tkk = tk.tkk
def convert():
    mile_input = entry_int.get()
    km_output = mile_input*1.61
    output_str.set(km_output)

# Window
# window = tk.Tk()
window = ttk.Window(themename="darkly")
window.title("Demo")
# widthxheight
window.geometry("300x150")

# The pack order determines the horizontal placement
# Title
title_label = ttk.Label(master=window, text = "Miles to kilometers", font = 'Calibri 24 bold')
title_label.pack()

# Input
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entry_int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
# Packs the widgets into the frame
entry.pack(side='left', padx = 10)
button.pack(side='left')
input_frame.pack(pady = 10)

# Output
output_str = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text = 'Output',
    font = 'Calibri 24',
    textvariable=output_str
)
output_label.pack(pady = 5)
# Run
window.mainloop()
