import tkinter as tk
from ttkbootstrap import ttk
# from tkinter import ttk

window = tk.Tk()
window.title('Pack parenting')
window.geometry('600x500')

# Top widgets
top_frame = tk.Frame(window)
label1 = ttk.Label(top_frame, text="Label 1", background='red')
label2 = ttk.Label(top_frame, text="Label 2", background="green")

label1.pack(side = 'left', fill = 'both', expand = True)
label2.pack(side = 'left', fill = 'both', expand = True)

# Middle widgets
label3 = ttk.Label(window, text="Label 3", background="blue")

# Bottom widgets
bottom_frame = tk.Frame(window)
label4 = ttk.Label(bottom_frame, text="Label 3", background="orange")
button1 = ttk.Button(bottom_frame, text="Button 1")
button2 = ttk.Button(bottom_frame, text = "Button2")
label4.pack(side =  'left', expand=True, fill = 'both')
button1.pack(side = 'left', expand=True, fill = 'both')
button2.pack(side = 'left', expand=True, fill = 'both')

# Ex widget
right_bottom_frame = tk.Frame(bottom_frame)
button3 = ttk.Button(right_bottom_frame, text="Button 3")
button4 = ttk.Button(right_bottom_frame, text = "Button 4")
button5 = ttk.Button(right_bottom_frame, text="Button 5")
button3.pack(expand=True, fill = 'both', padx = 10, pady = 10)
button4.pack(expand=True, fill = 'both', padx = 10, pady = 10)
button5.pack(expand=True, fill = 'both', padx = 10, pady = 10)

right_bottom_frame.pack(side = 'left', expand = True, fill = 'both')
top_frame.pack(fill = "both", expand = True)
label3.pack(expand = True)
bottom_frame.pack(expand = True, fill = 'both', padx = 20, pady = 20)

window.mainloop()