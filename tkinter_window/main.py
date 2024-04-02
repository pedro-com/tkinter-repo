import tkinter as tk
from tkinter import ttk

window = tk.Tk()
w_width = 600
h_height = 600
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f'{w_width}x{h_height}+{int(width/2- w_width/2)}+{int(height/2 - h_height/2)}')

# window.iconbitmap('set an ico file')
window.minsize(200, 100)
window.maxsize(800, 700)
window.resizable(True, False)

# Screen attributs
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# Window attributes
window.attributes('-alpha', 0.1) # Transparency
window.attributes('-topmost', True)
window.bind('<Escape>', lambda event: window.quit())

# window.attributes('-disable', True)
# window.attributes("-fullscreen", True)

window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx = 1.0, rely = 1.0, anchor = 'se')
window.mainloop()