from tkinter import *
import socket


tabIp = ['127.0.0.1','127.0.0.1','127.0.0.1','127.0.0.1']
list = []
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE_START = "start"
MESSAGE_STOP = "stop"

def cb():
    for i in range(0,len(tabIp)):
        if list[i].get() :
            #envoi d'une requete de lancement
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((tabIp[i], TCP_PORT))
            s.send(MESSAGE_START.encode())
        else :
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((tabIp[i], TCP_PORT))
            s.send(MESSAGE_STOP.encode())
            s.close()


fenetre = Tk()
fenetre['bg']='white'
p = PanedWindow(fenetre, orient=VERTICAL)
p.pack(side=TOP, expand=Y, fill=BOTH, pady=2, padx=2)
for i in range(0,len(tabIp)):
    v = BooleanVar();
    list.append(v)
    l = LabelFrame(p, text="STM32 .../IP", padx=20, pady=20)
    l.pack(fill="both", expand="yes")
    Label(l, text=tabIp[i]).pack()
    cbox = Checkbutton(l, text='Activer', var=v)
    cbox.pack()
Button(fenetre, text='Configure', command=cb).pack()
fenetre.mainloop()
