import customtkinter as ctk

app = ctk.CTk()

app.geometry('350x350')
radio1 = ctk.CTkRadioButton(app, text="Option A")
radio2 = ctk.CTkRadioButton(app, text="Option B")
radio1.pack()
radio2.pack()

app.mainloop()