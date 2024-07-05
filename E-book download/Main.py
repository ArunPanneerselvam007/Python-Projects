from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pg1 as p
m=Tk()
m.title("PuthagaChozhai E-Book Shopping")
m.geometry("800x600")
m.configure(bg='skyblue')
t=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil.png",height=100,width=150)
e=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english.png",width=150)
#lo=m.iconphoto(True,ic)
l1=Label(m,text="Welcome TO \n Puthagachozhai E-book shopping",font='Broadway',bg='pink',fg='Black')
l1.place(x=200,y=100)
l2=Label(m,text="Inidhai Karpom....!\n \t  Arram Payilvom....",font='times_new_roman',bg='lightgreen',fg='Red')
l2.place(x=350,y=180)
def but():
	m1=Toplevel()
	m1.title("Next")
	m1.geometry("300x300")
	i=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\pic.png")
	img=Label(image=i)
	img.pack()
	return ""
l3=Label(m,text="Which Language Do You Prefer ?",font='times_new_roman',bg='skyblue')
l3.place(x=200,y=300)
'''l2=Label(m,text="Inidhai Karpom....!\n \t  Arram Payilvom....",font='times_new_roman',bg='lightgreen',fg='Red')
l2.place(x=100,y=120)'''
	
b=Button(m,image=t,command=p.tamil)
b.place(x=250,y=350)
b1=Button(m,image=e,command=p.english)
b1.place(x=450,y=350)
m.mainloop()
