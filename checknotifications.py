import win10toast, datetime



def send_noti_whit_date(y,mo,d,h,m,s):
    noti = win10toast.ToastNotifier()
    fecha_noti=datetime.datetime(y,mo,d,h,m,s)
    while True:
        fecha_actual = datetime.datetime.now()
        fecha_actual_texto=fecha_actual.strftime("%d/%m/%Y, %H:%M:%S")
        fecha_noti_texto=fecha_noti.strftime("%d/%m/%Y, %H:%M:%S")
        print(fecha_actual_texto)
        if str(fecha_actual_texto) == str(fecha_noti_texto):
            noti.show_toast("hola", "lo tienes pendiente", threaded=True)

#send_noti_whit_date(2022,11,30,16,39,0)