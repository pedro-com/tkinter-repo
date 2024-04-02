import tkinter as tk
from tkinter import ttk

'''
    You bind events to the widget (modifier-type-detail)
    https://www.pythontutorial.net/tkinter/tkinter-event-binding/
'''
def get_pos(event):
    print(f'x: {event.x}, y: {event.y}')
window = tk.Tk()
window.geometry('600x500')
window.title('Event binding')

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text='Button')
button.pack()

# window.bind('<Alt-KeyPress-a>', lambda event: print(event))
# The events only run when you are in the widget or the window
button.bind('<KeyPress-a>', lambda event: print(event))
window.bind('<KeyPress>', lambda event: print(f'{event.char}'))
# window.bind('<Motion>', get_pos)
text.bind('<MouseWheel>', lambda event: print('MouseWheel'))
entry.bind('<FocusIn>', lambda event: print("Was focused"))


window.mainloop()