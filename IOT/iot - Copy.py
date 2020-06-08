import tkinter
from tkinter import *
import mysql.connector as mcon
#import RPi.GPIO as led #library for gpio pins
#led.setwarnings(False) #remove the warnings
#import time #import time delay
#led.setmode(led.BCM) #mode is set as bcm
#led.setup(2,OUT) #GPIO 2 is made OUTPUT
root=tkinter.Tk()
root.geometry("1366x768+0+0")
root.title("Internet Of Things")
mi=PhotoImage(file="iot.gif")
L1=Label(root,image=mi)
L1.place(x=0,y=0)
bit=mcon.connect(host="localhost",database="iot",user="root",password="3998")
def bulb():
    cursor=bit.cursor()
    x=messagebox.askyesno(title="Message",message="Turn the lights ON?")
    if(x==True):
        messagebox.showinfo(title="status",message="Lights ON..!!")
        cmd="UPDATE DEViCES SET STATUS='ON' WHERE ID=1;"
        cursor.execute(cmd)
        bit.commit()
        cursor.close()
     #   led.output(2,True)
    else:
        messagebox.showinfo(title="status",message="Lights OFF..!!")
        cmd="UPDATE DEViCES SET STATUS='OFF' WHERE ID=1;"
        cursor.execute(cmd)
        bit.commit()
        cursor.close()
     #   led.output(2,False)
def fans():
    x=messagebox.askyesno(title="Message",message="Turn the fan ON?")
    cursor=bit.cursor()
    if(x==True):
        messagebox.showinfo(title="status",message="Fan ON..!!")
        cmd="UPDATE DEViCES SET STATUS='ON' WHERE ID=2;"
        cursor.execute(cmd)
        bit.commit()
        cursor.close()
     #   led.output(2,True)
    else:
        messagebox.showinfo(title="status",message="Fan OFF..!!")
        cmd="UPDATE DEViCES SET STATUS='OFF' WHERE ID=2;"
        cursor.execute(cmd)
        bit.commit()
        cursor.close()
     #   led.output(2,False)
def cooler():
    x=messagebox.askyesno(title="Message",message="Turn the cooler ON?")
    cursor=bit.cursor()
    if(x==True):
        messagebox.showinfo(title="status",message="Cooler ON..!!")
        cmd="UPDATE DEViCES SET STATUS='ON' WHERE ID=3;"
        cursor.execute(cmd)
        bit.commit()
        cursor.close()
     #   led.output(2,True)
    else:
        messagebox.showinfo(title="status",message="Cooler OFF..!!")
        cmd="UPDATE DEViCES SET STATUS='OFF' WHERE ID=3;"
        cursor.execute(cmd)
        bit.commit()
        cursor.close()
     #   led.output(2,False)
def motor():
    x=messagebox.askyesno(title="Message",message="Turn the Motor ON?")
    cursor=bit.cursor()
    if(x==True):
        messagebox.showinfo(title="status",message="Motor ON..!!")
        cmd="UPDATE DEViCES SET STATUS='ON' WHERE ID=4;"
        cursor.execute(cmd)
        bit.commit()
        cursor.close()
     #   led.output(2,True)
    else:
        messagebox.showinfo(title="status",message="Motor OFF..!!")
        cmd="UPDATE DEViCES SET STATUS='OFF' WHERE ID=4;"
        cursor.execute(cmd)
        bit.commit()
        cursor.close()
     #   led.output(2,False)
A1=Button(root,text="Bulbs",font=("Old English Text MT",24),fg="white",bg="indigo",command=bulb)
A1.pack()
A1.place(x=250,y=600)
A2=Button(root,text="Fans",font=("Old English Text MT",24),fg="white",bg="indigo",command=fans)
A2.pack()
A2.place(x=500,y=600)
A3=Button(root,text="Cooler",font=("Old English Text MT",24),fg="white",bg="indigo",command=cooler)
A3.pack()
A3.place(x=790,y=600)
A4=Button(root,text="Motor",font=("Old English Text MT",24),fg="white",bg="indigo",command=motor)
A4.pack()
A4.place(x=1050,y=600)
root.mainloop()
