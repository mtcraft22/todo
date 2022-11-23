import tkinter
notis=[]
class noti:
    def __init__(self,**kwargs):
        self.date=kwargs["date"]
        self.description=kwargs["description"]
        self.tittle=kwargs["title"]
        self.priority=kwargs["priority"]
        self.label=None
        notis.append(self)
    def make_label(self,canvas):  
        print(notis)
        self.label=tkinter.Label(canvas,bg="white",text=self.tittle)
        self.label.grid(row=notis.index(notis[-1])+1,column=0)
        self.label.bind("<Button-1>",self.show_info)
    def show_info(self, event):
        self.info=tkinter.Toplevel()
        label0=tkinter.Label(self.info,text="Descrición: ").grid(row=1,column=0)
        label1=tkinter.Label(self.info,text=self.description).grid(row=1,column=1)
        label2=tkinter.Label(self.info,text="Fecha notificación: ").grid(row=2,column=0)
        label3=tkinter.Label(self.info,text=self.date).grid(row=2,column=1)
        buttondel=tkinter.Button(self.info,text="Eliminar tarea",command=self.removenoti).grid(row=3,column=0)
    def removenoti(self):
        self.info.destroy()
        self.label.destroy()
        notis.remove(self)
        del(self)

