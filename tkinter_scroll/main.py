import tkinter as tk
import ttkbootstrap as ttk
from random import randint, choice
window = tk.Tk()
window.geometry('600x400')
window.title('Scrolling')


canvas = tk.Canvas(window, bg = 'red', scrollregion=(0, 0, 2000, 5000))
canvas.create_line(0, 0, 2000, 5000, color='green', width = 1)
for i in range(100):
    l = randint(0, 2000)
    t = randint(0, 5000)
    r = l + randint(10, 500)
    b = t + randint(10, 500)
    color = choice(('red', 'green', 'blue', 'yellow', 'orange'))
    canvas.create_rectangle(l, t, r, b, fill = color)
canvas.pack(expand = True, fill = 'both')

canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 60), "units"))
scrollbar = ttk.Scrollbar(window, orient = 'vertical', command = canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx = 1, rely = 0, relheight=1, anchor = 'ne')

scrollbarh = ttk.Scrollbar(window, orient = 'horizontal', command = canvas.xview)
canvas.configure(xscrollcommand=scrollbar.set)
scrollbarh.place(relx = 0, rely = 1, relwidth=0.99, anchor = 'ne')
canvas.bind('<Control MouseWheel>', lambda event: canvas.xview_scroll(int(event.delta / 60), "units"))

text = tk.Text(window)
for i in range(1, 200):
    text.insert(f'{i}.0', f'text: {i}\n')
window.mainloop()