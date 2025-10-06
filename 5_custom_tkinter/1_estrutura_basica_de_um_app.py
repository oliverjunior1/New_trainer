import customtkinter as ctk

ctk.set_appearance_mode("dark")

ctk.set_default_color_theme('blue')

# Criar a janela principal

app = ctk.CTk()
app.geometry("400x300")
app.title("Minha Interface Moderna")

# Adicionar um botão

botao = ctk.CTkButton(app, text="Clique aqui")
botao.pack(pady=20)

# Rodar a aplicação

app.mainloop()