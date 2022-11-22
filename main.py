import tkinter,noti

root=tkinter.Tk()
root.geometry("800x800")

hasnotified=tkinter.IntVar()

listanotis=tkinter.Canvas(root,bg="white").grid(row=0,column=0,rowspan=100)
tittle_label=tkinter.Label(root,text="  Nombre: ").grid(row=0,column=1,padx=2)
tittle_entry=tkinter.Entry(root,width=32)
tittle_entry.grid(row=0,column=2,padx=2)
desc_label=tkinter.Label(root,text="Descrición: ").grid(row=1,column=1,padx=2)
desc_entry=tkinter.Text(root,height=5,width=32)
desc_entry.grid(row=1,column=2,padx=2,rowspan=4)

Date_label=tkinter.Label(root,text="Fecha: ").grid(row=7,column=1,padx=2)
Date_entry=tkinter.Entry(root,width=32,state='disabled')
Date_entry.grid(row=7,column=2,padx=2)
def enable(hasnotifiedp):
    print(hasnotifiedp)
    adv_label=tkinter.Label(root,text="  ")
    adv_label.grid(row=5,column=1,padx=2)
    if hasnotifiedp.get()==0:
        Date_entry.config(state='disabled')
        desc_label
    else:
        Date_entry.config(state='normal')
def get_all():
    tittle=tittle_entry.get()
    desc=desc_entry.get(1.0,tkinter.END)
    date=Date_entry.get()
    print(tittle)
    if tittle:
        a=noti.noti(title=tittle,date=date,description=desc,priority=None)
        a.make_label(listanotis)

   

noticheck=tkinter.Checkbutton(root,text="Quiero recibir una notificación de la tarea (WIP)",variable=hasnotified,command=lambda:enable(hasnotified)).grid(row=6,column=2,padx=2)
Submit=tkinter.Button(root,text="Añadir tarea",command=get_all).grid(row=5,column=2,padx=2)
root.mainloop()