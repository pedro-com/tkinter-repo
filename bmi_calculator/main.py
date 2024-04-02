from typing import Any, Tuple
import customtkinter as ctk
from settings import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        super().__init__(fg_color = GREEN)
        self.title('BMI Calculator')
        self.geometry('400x400')
        self.resizable(False, False)
        self.columnconfigure(0, weight = 1)
        self.rowconfigure((0, 1, 2, 3), weight = 1, uniform='a')
        ResultText(self).grid(row = 0, column = 0, rowspan = 0, colspan = 2, sticky = 'nswe')
        WeightInput(self).grid(row = 0, column = 2, rowspan = 0, colspan = 1, sticky = 'nswe')
        self.mainloop()

class ResultText(ctk.CTkLabel):
    def __init__(self, parent):
        font = ctk.CTkFont(family = FONT, size = MAIN_TEXT_SIZE, weight = 'bold')
        super().__init__(parent, text = 22.5, font = font, text_color = WHITE)

class WeightInput(ctk.CtkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.font = ctk.CTkFont(family = FONT, size = INPUT_FONT_SIZE)
        self.rowconfigure(0, weight = 1, uniform = 'b')
        self.columnconfigure((0, 4), weight = 2, uniform = 'b')
        self.columnconfigure(2, weight = 3, uniform = 'b')
        self.columnconfigure((1, 3), weight = 2, uniform = 'b')
        label = ctk.CTkLabel(self, text = '70kg', text_color=BLACK, font = self.font)
        create_button('-', 0, 0, )

        def create_button(self, text, row, column, pad):
            button = ctk.CTkButton(self, text = text, font = self.font, text_color = BLACK, fg_color= WHITE, hover_color=LIGHT_GRAY)
            button.grid(row = row, column = column, padx = pad, pady = pad)




if __name__ == '__main__':
    App()