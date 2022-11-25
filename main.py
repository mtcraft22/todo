import tkinter, noti

meses=[]
class todo_main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("800x800")

        self.hasnotified = tkinter.IntVar()
        self.setpriority = tkinter.IntVar()
        self.priority_level = tkinter.StringVar()

        self.listanotis = tkinter.Canvas(self.root, bg="white", width=200, height=10000).grid(row=0, column=0,
                                                                                              rowspan=1000, padx=5,
                                                                                              pady=5)

        self.tittle_label = tkinter.Label(self.root, text="  Nombre: ")
        self.tittle_label.grid(row=0, column=1, padx=2)

        self.tittle_entry = tkinter.Entry(self.root, width=32)
        self.tittle_entry.grid(row=0, column=2, padx=2, columnspan=4)

        self.desc_label = tkinter.Label(self.root, text="Descrición: ")
        self.desc_label.grid(row=1, column=1, padx=2)

        self.desc_entry = tkinter.Text(self.root, height=5, width=32)
        self.desc_entry.grid(row=1, column=2, padx=2, rowspan=4, columnspan=4)

        self.Submit = tkinter.Button(self.root, text="Añadir tarea", command=self.get_all)

        self.Submit.grid(row=5, column=2, padx=2, columnspan=4)

        self.noticheck = tkinter.Checkbutton(self.root, text="Quiero recibir una notificación de la tarea (WIP)",
                                             variable=self.hasnotified, command=lambda: self.enable(self.hasnotified))

        self.noticheck.grid(row=6, column=2, padx=2, columnspan=4)

        self.priocheck = tkinter.Checkbutton(self.root, text="No quiero establecer una pioridad",
                                             variable=self.setpriority, command=lambda: self.enable_priority())

        self.priocheck.grid(row=7, column=2, padx=2, columnspan=4)
        
        self.Date_label = tkinter.Label(self.root, text="Fecha: ")
        self.Date_label.grid(row=8, column=1, padx=2)

        self.Date_entry = tkinter.Entry(self.root, width=32, state='disabled')
        self.Date_entry.grid(row=8, column=2, padx=2, columnspan=4)

        self.priority_label = tkinter.Label(self.root, text="Priodidad: ")
        self.priority_label.grid(row=9, column=1, padx=2)
    
        self.priority_level_0 = tkinter.Radiobutton(self.root, text="Baja", variable=self.priority_level, value="Baja",
                                                    tristatevalue=" ")
        self.priority_level_0.grid(row=9, column=2, padx=2)

        self.priority_level_1 = tkinter.Radiobutton(self.root, text="Media", variable=self.priority_level, value="Media"
                                                    , tristatevalue=" ")
        self.priority_level_1.grid(row=9, column=3, padx=2)

        self.priority_level_2 = tkinter.Radiobutton(self.root, text="Alta", variable=self.priority_level, value="Alta"
                                                    , tristatevalue=" ")
        self.priority_level_2.grid(row=9, column=4, padx=2)

        self.priority_level_3 = tkinter.Radiobutton(self.root, text="Urgente", variable=self.priority_level,
                                                    value="Urgente", tristatevalue=" ")
        self.priority_level_3.grid(row=9, column=5, padx=2)
        self.root.mainloop()

    def enable(self, hasnotifiedp):
        adv_label = tkinter.Label(self.root, text="  ")
        adv_label.grid(row=5, column=1, padx=2)
        if hasnotifiedp.get() == 0:
            self.Date_entry.config(state='disabled')
        else:
            self.Date_entry.config(state='normal')
    def enable_priority(self):
        if self.setpriority.get()== 0:
            self.priority_level_0.config(state='normal')
            self.priority_level_1.config(state='normal')
            self.priority_level_2.config(state='normal')
            self.priority_level_3.config(state='normal')
        else:
            self.priority_level_0.config(state='disabled')
            self.priority_level_1.config(state='disabled')
            self.priority_level_2.config(state='disabled')
            self.priority_level_3.config(state='disabled')
    def get_all(self):
        tittle = self.tittle_entry.get()
        desc = self.desc_entry.get(1.0, tkinter.END)
        date = self.Date_entry.get()
        if tittle:
            a = noti.noti(title=tittle, date=date, description=desc, priority=self.priority_level.get())
            a.make_label(self.listanotis)


app = todo_main()
