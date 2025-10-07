# Crie uma interface com:
# • 	Um campo para digitar o nome.
# • 	Um botão “Enviar” que imprime o nome no terminal.
# • 	Um rótulo que muda para “Olá, [nome]!” após o clique.

import customtkinter as ctk

app = ctk.CTk()

app.geometry('500x500')
entry = ctk.CTkEntry(app, placeholder_text="Put your name: ")
entry.pack()
button = ctk.CTkButton(app, text="Enviar", command=lambda: print(f"Hi, {entry.get()}!"))
button.pack()

app.mainloop()