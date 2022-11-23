import tkinter,noti


class todo_main:
    def __init__(self):
        self.root=tkinter.Tk()
        self.root.geometry("800x800")

        self.hasnotified=tkinter.IntVar()
        self.priority_level=tkinter.IntVar()

        self.listanotis=tkinter.Canvas(self.root,bg="white").grid(row=0,column=0,rowspan=100)

        self.tittle_label=tkinter.Label(self.root,text="  Nombre: ").grid(row=0,column=1,padx=2)

        self.tittle_entry=tkinter.Entry(self.root,width=32)
        self.tittle_entry.grid(row=0,column=2,padx=2,columnspan=4)

        self.desc_label=tkinter.Label(self.root,text="Descrición: ").grid(row=1,column=1,padx=2)

        self.desc_entry=tkinter.Text(self.root,height=5,width=32)
        self.desc_entry.grid(row=1,column=2,padx=2,rowspan=4,columnspan=4)

        self.Date_label=tkinter.Label(self.root,text="Fecha: ").grid(row=7,column=1,padx=2)

        self.Date_entry=tkinter.Entry(self.root,width=32,state='disabled')
        self.Date_entry.grid(row=7,column=2,padx=2,columnspan=4)

        self.noticheck=tkinter.Checkbutton(self.root,text="Quiero recibir una notificación de la tarea (WIP)",variable=self.hasnotified,command=lambda:self.enable(self.hasnotified)).grid(row=6,column=2,padx=2,columnspan=4)
        
        self.Submit=tkinter.Button(self.root,text="Añadir tarea",command=self.get_all).grid(row=5,column=2,padx=2,columnspan=4)
        
        self.priority_label=tkinter.Label(self.root,text="Priodidad: ").grid(row=8,column=1,padx=2)

        self.priority_level_0=tkinter.Radiobutton(self.root,text="Baja",variable=self.priority_level,value=0).grid(row=8,column=2,padx=2) 
        self.priority_level_0=tkinter.Radiobutton(self.root,text="Media",variable=self.priority_level,value=1).grid(row=8,column=3,padx=2)
        self.priority_level_0=tkinter.Radiobutton(self.root,text="Alta",variable=self.priority_level,value=2).grid(row=8,column=4,padx=2)
        self.priority_level_0=tkinter.Radiobutton(self.root,text="Urgente",variable=self.priority_level,value=3).grid(row=8,column=5,padx=2)

        self.root.mainloop()
    def enable(self,hasnotifiedp):
        adv_label=tkinter.Label(self.root,text="  ")
        adv_label.grid(row=5,column=1,padx=2)
        if hasnotifiedp.get()==0:
            self.Date_entry.config(state='disabled')
        else:
            self.Date_entry.config(state='normal')
    def get_all(self):
        tittle=self.tittle_entry.get()
        desc=self.desc_entry.get(1.0,tkinter.END)
        date=self.Date_entry.get()
        if tittle:
            a=noti.noti(title=tittle,date=date,description=desc,priority=None)
            a.make_label(self.listanotis)


app=todo_main()
