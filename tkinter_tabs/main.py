import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title("Tab widget")

notebook = ttk.Notebook(window)
# Tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text = "Label in tab 1")
label1.pack()
button1 = ttk.Button(tab1, text = 'Button in tab 1')
button1.pack()

# Tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = "Label in tab 2")
label2.pack()
button2 = ttk.Button(tab2, text = 'Button in tab 2')
button2.pack()

# Tab 2
tab3 = ttk.Frame(notebook)
label3 = ttk.Label(tab3, text = "Label in tab 3")
label3.pack()
button3 = ttk.Button(tab3, text = 'Button in tab 3, 1')
button3.pack()
button4 = ttk.Button(tab3, text = 'Button in tab 3, 2')
button4.pack()

notebook.add(tab1, text = "Tab 1")
notebook.add(tab2, text = "Tab 2")
notebook.add(tab3, text = "Tab 3")

notebook.pack()


window.mainloop()