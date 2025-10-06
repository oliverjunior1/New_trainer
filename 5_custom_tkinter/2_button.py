import customtkinter as ctk

app = ctk.CTk()
botao = ctk.CTkButton(app, text="Enviar", command=lambda: print("Enviando!"))
botao.pack()


app.mainloop()