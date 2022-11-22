import win10toast, datetime

import tkinter as tk

noti = win10toast.ToastNotifier()
fecha_noti=datetime.datetime(2022,11,22,12,39,0)
while True:
    fecha_actual = datetime.datetime.now()
    fecha_actual_texto=fecha_actual.strftime("%d/%m/%Y, %H:%M:%S")
    fecha_noti_texto=fecha_noti.strftime("%d/%m/%Y, %H:%M:%S")
    print(fecha_actual_texto)
    if str(fecha_actual_texto) == str(fecha_noti_texto):
        noti.show_toast("hola", "lo tienes pendiente", threaded=True)