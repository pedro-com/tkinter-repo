import customtkinter as ctk

window = ctk.CTk()
window.title("Custom tkinter")
window.geometry("600x400")

label = ctk.CTkLabel(window, text = "Ctk Label", fg_color = "red", text_color="white", corner_radius=10).pack()

button = ctk.CTkButton(window, text = "Ctk Button", fg_color ='#FF0', hover_color='#AA0', command = lambda: ctk.set_appearance_mode('light')).pack()

frame = ctk.CTkFrame(window)
frame.pack()
slider = ctk.CTkSlider(frame)
window.mainloop()