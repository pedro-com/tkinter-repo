import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
window = tk.Tk()
window.title('Sliders')

scale_int = tk.IntVar(value = 15)
scale = ttk.Scale(window,
    command= lambda value: print(value),
    from_ = 0,
    to = 25,
    length = 300,
    orient='horizontal', # vertical
    variable = scale_int,
)
scale.pack()

# Progress bar
progress = ttk.Progressbar(window,
    variable = scale_int,
    maximum = 25,
    mode = 'determinate', # 'indeterminate',
    length = 400
)
progress.pack()

# progress.start(1000)

# Scrolled text
scrolled_text = scrolledtext.ScrolledText(window, width = 100, height = 5)
scrolled_text.pack()

window.mainloop()