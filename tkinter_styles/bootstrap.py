import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter
'''
ttkbootstrap
    python -m ttkcreator
'''
window = ttk.Window(themename = 'darkly')
window.title("ttk bootstrap intro")
window.geometry('600x600')

label = ttk.Label(window, text = "Label", bootstyle = 'danger-outline')

scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand = True)

for i in range(100):
    ttk.Label(scroll_frame, text = f'Label: {i}')
    ttk.Button(scroll_frame, text = 'Button')


toast = ToastNotification(title = "This is the title", message = "This is the actual message", duration = 2000, bootstyle = 'dark', position = (0, 0, 'sw'))

# Tooltip
button = ttk.Button(window, text = "Button", bootstyle="warning")
button.pack(pady=10)
ToolTip(button, text = "This does nothing", bootstyle="danger-inverse")

calendar = DateEntry(window)
calendar.pack(pady = 10)
ttk.Button(window, text = "Calendar date", command = lambda: print(calendar.entry.get())).pack()

progress_int = tk.IntVar(value = 50)
progress = ttk.Floodgauge(
    window,
    text = 'progress',
    variable = progress_int,
    bootstyle='danger',
    mask = 'mask {}·'
).pack()
ttk.Scale(window, from_ = 0, to= 100, variable=progress_int).pack()

window.mainloop()