import customtkinter as ctk

app = ctk.CTk()
app.geometry('500x500')
frame = ctk.CTkFrame(app)
frame.pack(pady=10)
ctk.CTkLabel(frame, text="Dentro do frame").pack()


app.mainloop()