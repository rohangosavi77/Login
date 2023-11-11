from tkinter import *
import time
from tkinter import messagebox

# def click():
#     messagebox.showinfo(title="MegaSpark",message="Your Login is Sucessful !")

def click():
    name = "Rohan"
    passw = "Password"
    if username.get() == name and password.get() == passw:
         messagebox.showinfo(title="MegaSpark",message="Your Login is Sucessful !")
         print("New Account : "+name)
         print("Password : "+passw)
    else:
         messagebox.showinfo(title="MegaSpark",message="Login Failed !")
        

window = Tk()
window.title("Login GUI")
window.geometry("600x383")
window.resizable(False,False)

image1 = PhotoImage(file="D:\Code\Projects\Login\image.png")
label = Label(window,image=image1)
label.pack()
label.place(x=0,y=0)

label1 = Label(window
                ,height="1"
                ,width="10"
                ,text="username"
                ,activebackground="white"
                ,activeforeground="black"
                ,fg="black"
                ,bg="white"
                ,font=("consolas",15))
label1.pack()
label1.place(x=19,y=108)

label2 = Label(window
                ,height="1"
                ,width="10"
                ,text="password"
                ,activebackground="white"
                ,activeforeground="black"
                ,fg="black"
                ,bg="white"
                ,font=("consolas",15))
label2.pack()
label2.place(x=19,y=187)

username = Entry(window,font=("consolas",12),borderwidth=2)
username.pack()
username.place(x=31,y=140)

password = Entry(window,show="*",font=("consolas",12),borderwidth=2)
password.pack()
password.place(x=31,y=220)

button = Button(window,text="Login",font=("Arial",12),width=7,height=1,command=click)
button.pack()
button.place(x=148,y=260)

label3 = Label(window,text="Login Up",font=("Script MT Bold",21),bg="white",fg="black")
label3.pack()
label3.place(x=70,y=40)

window.mainloop()

