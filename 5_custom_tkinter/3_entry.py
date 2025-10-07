import customtkinter as ctk

app = ctk.CTk()

entry = ctk.CTkEntry(app, placeholder_text="Digite seu nome: ")
entry.pack()
button = ctk.CTkButton(app, text='Enviar', command=lambda: print(f"Hi, {entry.get()}!"))
button.pack()
app.mainloop()