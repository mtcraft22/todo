import tkinter
import tkinter.messagebox
import customtkinter


class app():
    def __init__(self):
        self.CTk = customtkinter.CTk()
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("blue")

        self.contentcavas = customtkinter.CTkLabel(master=self.CTk, bg_color="#99cae1")
        self.contentcavas.grid(row=0, column=0, rowspan=10,pady=5,padx=5)
        self.noticanvas = tkinter.Canvas(master=self.contentcavas, height=500, bg="#99cae1", highlightthickness=0)
        self.noticanvas.grid(row=0, column=0)

        self.Tittle = customtkinter.CTkEntry(master=self.CTk)
        self.Tittle.grid(row=0, column=2)
        self.Tittle_label = customtkinter.CTkLabel(master=self.CTk, text="Titulo: ")
        self.Tittle_label.grid(row=0, column=1)

        self.descrition = customtkinter.CTkTextbox(master=self.CTk, border_color="grey", border_width=2.5)
        self.descrition.grid(row=1, column=2)
        self.CTk.mainloop()


App = app()
