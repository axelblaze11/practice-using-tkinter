import tkinter
from tkinter import *
import mysql.connector as mcon
root=tkinter.Tk()
root.geometry("1366x768+0+0")
root.title("Login Page")
bit=mcon.connect(host="localhost",database="iot",user="root",password="3998")
mi=PhotoImage(file="Aman.gif")
L3=Label(root,image=mi,font=("arial",15),bg="black",fg="white")
L3.place(x=0,y=0)
E1=Entry(root,font=("Comic Sans MS",18),fg="green")
E1.place(x=725,y=245)
E2=Entry(root,font=("Comic Sans MS",18),fg="red",show="♥")
E2.place(x=725,y=350)
def axel():
    x=E1.get()
    y=E2.get()
    if x=="Axel":
        if y=="176044":
            messagebox.showinfo(message="Hello Axel!!",title="INFO!")
            aa=Toplevel(root)
            aa.geometry("1366x768+0+0")
            aa.title("Internet Of Things")
            mi2=PhotoImage(file="iot.gif")
            L1=Label(aa,image=mi2)
            L1.place(x=0,y=0)
            def bulb():
                cursor=bit.cursor()
                x=messagebox.askyesno(title="Message",message="Turn the lights ON?")
                if(x==True):
                    messagebox.showinfo(title="status",message="Lights ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=1;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Lights OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=1;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            def fans():
                x=messagebox.askyesno(title="Message",message="Turn the fan ON?")
                cursor=bit.cursor()
                if(x==True):
                    messagebox.showinfo(title="status",message="Fan ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=2;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Fan OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=2;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            def cooler():
                x=messagebox.askyesno(title="Message",message="Turn the cooler ON?")
                cursor=bit.cursor()
                if(x==True):
                    messagebox.showinfo(title="status",message="Cooler ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=3;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Cooler OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=3;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            def motor():
                x=messagebox.askyesno(title="Message",message="Turn the Motor ON?")
                cursor=bit.cursor()
                if(x==True):
                    messagebox.showinfo(title="status",message="Motor ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=4;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Motor OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=4;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            A1=Button(aa,text="Bulbs",font=("Old English Text MT",24),fg="white",bg="indigo",command=bulb)
            A1.pack()
            A1.place(x=250,y=600)
            A2=Button(aa,text="Fans",font=("Old English Text MT",24),fg="white",bg="indigo",command=fans)
            A2.pack()
            A2.place(x=500,y=600)
            A3=Button(aa,text="Cooler",font=("Old English Text MT",24),fg="white",bg="indigo",command=cooler)
            A3.pack()
            A3.place(x=790,y=600)
            A4=Button(aa,text="Motor",font=("Old English Text MT",24),fg="white",bg="indigo",command=motor)
            A4.pack()
            A4.place(x=1050,y=600)
            aa.mainloop()
    elif x=="SiD":
        if y=="176036":
            messagebox.showinfo(message="Hello SiD!!",title="INFO!")
            aa=Toplevel(root)
            aa.geometry("1366x768+0+0")
            aa.title("Internet Of Things")
            mi2=PhotoImage(file="iot.gif")
            L1=Label(aa,image=mi2)
            L1.place(x=0,y=0)
            def bulb():
                cursor=bit.cursor()
                x=messagebox.askyesno(title="Message",message="Turn the lights ON?")
                if(x==True):
                    messagebox.showinfo(title="status",message="Lights ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=1;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Lights OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=1;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            def fans():
                x=messagebox.askyesno(title="Message",message="Turn the fan ON?")
                cursor=bit.cursor()
                if(x==True):
                    messagebox.showinfo(title="status",message="Fan ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=2;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Fan OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=2;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            def cooler():
                x=messagebox.askyesno(title="Message",message="Turn the cooler ON?")
                cursor=bit.cursor()
                if(x==True):
                    messagebox.showinfo(title="status",message="Cooler ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=3;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Cooler OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=3;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            def motor():
                x=messagebox.askyesno(title="Message",message="Turn the Motor ON?")
                cursor=bit.cursor()
                if(x==True):
                    messagebox.showinfo(title="status",message="Motor ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=4;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Motor OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=4;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            A1=Button(aa,text="Bulbs",font=("Old English Text MT",24),fg="white",bg="indigo",command=bulb)
            A1.pack()
            A1.place(x=250,y=600)
            A2=Button(aa,text="Fans",font=("Old English Text MT",24),fg="white",bg="indigo",command=fans)
            A2.pack()
            A2.place(x=500,y=600)
            A3=Button(aa,text="Cooler",font=("Old English Text MT",24),fg="white",bg="indigo",command=cooler)
            A3.pack()
            A3.place(x=790,y=600)
            A4=Button(aa,text="Motor",font=("Old English Text MT",24),fg="white",bg="indigo",command=motor)
            A4.pack()
            A4.place(x=1050,y=600)
            aa.mainloop()
    elif x=="Geetanshu":
        if y=="176070":
            messagebox.showinfo(message="Hello Geetanshu!!",title="INFO!")
            aa=Toplevel(root)
            aa.geometry("1366x768+0+0")
            aa.title("Internet Of Things")
            mi2=PhotoImage(file="iot.gif")
            L1=Label(aa,image=mi2)
            L1.place(x=0,y=0)
            def bulb():
                cursor=bit.cursor()
                x=messagebox.askyesno(title="Message",message="Turn the lights ON?")
                if(x==True):
                    messagebox.showinfo(title="status",message="Lights ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=1;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Lights OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=1;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            def fans():
                x=messagebox.askyesno(title="Message",message="Turn the fan ON?")
                cursor=bit.cursor()
                if(x==True):
                    messagebox.showinfo(title="status",message="Fan ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=2;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Fan OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=2;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            def cooler():
                x=messagebox.askyesno(title="Message",message="Turn the cooler ON?")
                cursor=bit.cursor()
                if(x==True):
                    messagebox.showinfo(title="status",message="Cooler ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=3;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Cooler OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=3;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            def motor():
                x=messagebox.askyesno(title="Message",message="Turn the Motor ON?")
                cursor=bit.cursor()
                if(x==True):
                    messagebox.showinfo(title="status",message="Motor ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=4;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Motor OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=4;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            A1=Button(aa,text="Bulbs",font=("Old English Text MT",24),fg="white",bg="indigo",command=bulb)
            A1.pack()
            A1.place(x=250,y=600)
            A2=Button(aa,text="Fans",font=("Old English Text MT",24),fg="white",bg="indigo",command=fans)
            A2.pack()
            A2.place(x=500,y=600)
            A3=Button(aa,text="Cooler",font=("Old English Text MT",24),fg="white",bg="indigo",command=cooler)
            A3.pack()
            A3.place(x=790,y=600)
            A4=Button(aa,text="Motor",font=("Old English Text MT",24),fg="white",bg="indigo",command=motor)
            A4.pack()
            A4.place(x=1050,y=600)
            aa.mainloop()
    elif x=="Rajendra":
        if y=="176026":
            messagebox.showinfo(message="Hello Rajendra!!",title="INFO!")
            aa=Toplevel(root)
            aa.geometry("1366x768+0+0")
            aa.title("Internet Of Things")
            mi2=PhotoImage(file="iot.gif")
            L1=Label(aa,image=mi2)
            L1.place(x=0,y=0)
            def bulb():
                cursor=bit.cursor()
                x=messagebox.askyesno(title="Message",message="Turn the lights ON?")
                if(x==True):
                    messagebox.showinfo(title="status",message="Lights ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=1;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()  
                else:
                    messagebox.showinfo(title="status",message="Lights OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=1;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            def fans():
                x=messagebox.askyesno(title="Message",message="Turn the fan ON?")
                cursor=bit.cursor()
                if(x==True):
                    messagebox.showinfo(title="status",message="Fan ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=2;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Fan OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=2;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            def cooler():
                x=messagebox.askyesno(title="Message",message="Turn the cooler ON?")
                cursor=bit.cursor()
                if(x==True):
                    messagebox.showinfo(title="status",message="Cooler ON..!!")
                    cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=3;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
                else:
                    messagebox.showinfo(title="status",message="Cooler OFF..!!")
                    cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=3;"
                    cursor.execute(cmd)
                    bit.commit()
                    cursor.close()
            def motor():
                 x=messagebox.askyesno(title="Message",message="Turn the Motor ON?")
                 cursor=bit.cursor()
                 if(x==True):
                     messagebox.showinfo(title="status",message="Motor ON..!!")
                     cmd="UPDATE DEViCE SET STATUS='ON' WHERE ID=4;"
                     cursor.execute(cmd)
                     bit.commit()
                     cursor.close()
                 else:
                     messagebox.showinfo(title="status",message="Motor OFF..!!")
                     cmd="UPDATE DEViCE SET STATUS='OFF' WHERE ID=4;"
                     cursor.execute(cmd)
                     bit.commit()
                     cursor.close()
            A1=Button(aa,text="Bulbs",font=("Old English Text MT",24),fg="white",bg="indigo",command=bulb)
            A1.pack()
            A1.place(x=250,y=600)
            A2=Button(aa,text="Fans",font=("Old English Text MT",24),fg="white",bg="indigo",command=fans)
            A2.pack()
            A2.place(x=500,y=600)
            A3=Button(aa,text="Cooler",font=("Old English Text MT",24),fg="white",bg="indigo",command=cooler)
            A3.pack()
            A3.place(x=790,y=600)
            A4=Button(aa,text="Motor",font=("Old English Text MT",24),fg="white",bg="indigo",command=motor)
            A4.pack()
            A4.place(x=1050,y=600)
            aa.mainloop()
    else:
        messagebox.showinfo(message="Invalid Username or Password!")
A1=Button(root,text="Log In",font=("Old English Text MT",24),fg="white",bg="indigo",command=axel)
A1.pack()
A1.place(x=650,y=500)

root.mainloop()
