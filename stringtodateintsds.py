def str2int(sateinput):
    firtsdiv=sateinput.split(", ")
    day=firtsdiv[0].split("/")
    time=firtsdiv[1].split(":")
    day.extend(time)
    return day



print(str2int("22/11/24, 9:1:0"))
