import customtkinter as ctk

app = ctk.CTk()

x = app.geometry("500x500")

label = ctk.CTkLabel(app, text="Jesus is the light of the world!")
label.pack()

app.mainloop()