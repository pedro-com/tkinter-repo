import customtkinter as ctk

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(parent, fg_color = 'red')
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = abs(start_pos - end_pos)

        self.pos = start_pos
        self.is_start = True
        self.place(relx = self.pos, rely = 0, relwidth = self.width, relheight = 1)
    
    def animate(self):
        # delta = (self.end_pos - self.start_pos)/(self.width * 4)
        if self.is_start:
            delta =  0.01 if self.end_pos > self.start_pos else -0.01
        else:
            delta =  -0.01 if self.start_pos > self.end_pos else 0.01
        # delta = 0.01 if self.end_pos > self.start_pos else -0.01
        self.is_start = not self.is_start
        self.after(10, lambda: self.move(delta))
    
    def move(self, delta):
        to_pos = self.start_pos if self.is_start else self.end_pos
        if self.pos < to_pos:
            self.pos += delta
            self.place(relx = self.pos, rely = 0, relwidth = self.width, relheight = 1)
            self.after(10, lambda: self.move(delta))
        
def move_button_an():
    global button_x
    button_x += 0.05
    if button_x < 0.9:
        button.place(relx = button_x, rely = 0.5, anchor = 'center')
        window.after(10, move_button_an)


def move_button():
    global button_x
    button_x += 0.05
    button.place(relx = button_x, rely = 0.5, relheight = button_x, anchor = 'center')

def infinite_print():
    print('infinite')
    window.after(1000, infinite_print)
window = ctk.CTk()
window.title('Animated widgets')
window.geometry('600x400')

button_x = 0.5
# button = ctk.CTkButton(window, text = 'toggle sidebar', command = move_button)
# button = ctk.CTkButton(window, text = 'toggle sidebar', command = infinite_print)
# button = ctk.CTkButton(window, text = 'toggle sidebar', command = move_button_an)

slide = SlidePanel(window, -0.3, 0)
button = ctk.CTkButton(window, text = 'toggle sidebar', command = slide.animate)

button.place(relx = button_x, rely = 0.5, relheight = button_x, anchor = 'center')
window.mainloop()