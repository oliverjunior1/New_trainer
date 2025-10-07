import customtkinter as ctk

app = ctk.CTk()

def change():
    ctk.CTkLabel(text="Jesus How I love you!")

label = ctk.CTkLabel(app, text="Jesus, I love you so much!")
label.pack()
button = ctk.CTkButton(app, text="Change", command=change)
button.pack()

app.mainloop()