from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pg2 as p2


def tamil():
	
	def nex():
		n1=Toplevel()
		n1.geometry("1400x1200")
		n1.configure(bg='skyblue')
		#Sci-Fictions
		l5=Label(n1,text=" Sciencefiction ",font='times_new_roman',bg='skyblue')
		l5.place(x=50,y=10)
		#i=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\logo.png",width=150)
		sc1=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\sc1.png",width=150,height=210)
		sc2=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\sc2.png",width=150,height=210)
		sc3=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\sc3.png",width=150,height=210)
		#sc4=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\f4.png",width=150,height=230)

		fb1=Button(n1,image=sc1,command=p2.down)
		fb1.place(x=50,y=50)
		fb2=Button(n1,image=sc2,command=p2.down)
		fb2.place(x=220,y=50)
		fb3=Button(n1,image=sc3,command=p2.down)
		fb3.place(x=390,y=50)
		#fb4=Button(n1,image=f4,command=down)
		#fb4.place(x=560,y=50)
		
		#Horror
		l6=Label(n1,text=" Horror ",font='times_new_roman',bg='skyblue')
		l6.place(x=50,y=270)
		#i=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\logo.png",width=150)
		h1=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\h1.png",width=150,height=210)
		h2=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\h2.png",width=150,height=210)
		h3=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\h3.png",width=150,height=210)
		h4=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\h4.png",width=150,height=210)

		hb1=Button(n1,image=h1,command=p2.down)
		hb1.place(x=50,y=300)
		hb2=Button(n1,image=h2,command=p2.down)
		hb2.place(x=220,y=300)
		hb3=Button(n1,image=h3,command=p2.down)
		hb3.place(x=390,y=300)
		hb4=Button(n1,image=h4,command=p2.down)
		hb4.place(x=560,y=300)

		n1.mainloop()
		
	x=Toplevel()
	x.title("Tamil Language")
	x.geometry("1400x1200")
	x.configure(bg='skyblue')
	l2=Label(x,text="Tamil Padaipupugal....",font='times_new_roman',bg='lightgreen',fg='Red')
	l2.place(x=450,y=30)
	
	#Historical
	l6=Label(x,text=" Historical ",font='times_new_roman',bg='skyblue')
	l6.place(x=50,y=70)
	#i=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\logo.png",width=150)
	hi1=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\hi1.png",width=150,height=210)
	hi2=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\hi2.png",width=150,height=210)
	hi3=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\hi3.png",width=150,height=210)
	hi4=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\hi4.png",width=150,height=210)

	hib1=Button(x,image=hi1,command=p2.down)
	hib1.place(x=50,y=100)
	hib2=Button(x,image=hi2,command=p2.down)
	hib2.place(x=220,y=100)
	hib3=Button(x,image=hi3,command=p2.down)
	hib3.place(x=390,y=100)
	hib4=Button(x,image=hi4,command=p2.down)
	hib4.place(x=560,y=100)
	
	
	#Fictions
	l4=Label(x,text="fiction ",font='times_new_roman',bg='skyblue')
	l4.place(x=50,y=350)
	#i=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\logo.png",width=150)
	f1=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\f1.png",width=150,height=220)
	f2=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\f2.png",width=150,height=220)
	f3=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\f3.png",width=150,height=220)
	f4=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\tamil\\f4.png",width=150,height=220)

	fb1=Button(x,image=f1,command=p2.down)
	fb1.place(x=50,y=380)
	fb2=Button(x,image=f2,command=p2.down)
	fb2.place(x=220,y=380)
	fb3=Button(x,image=f3,command=p2.down)
	fb3.place(x=390,y=380)
	fb4=Button(x,image=f4,command=p2.down)
	fb4.place(x=560,y=380)
	
	nb=Button(x,text="Next",command=nex)
	nb.place(x=100,y=700)
	
	
	
	x.mainloop()		
		
		

def english():
	
	def nex():
		n1=Toplevel()
		n1.geometry("1400x1200")
		n1.configure(bg='skyblue')
		#Sci-Fictions
		l5=Label(n1,text=" Sciencefiction ",font='times_new_roman',bg='skyblue')
		l5.place(x=50,y=10)
		#i=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\logo.png",width=150)
		sc1=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\sc1.png",width=150,height=210)
		sc2=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\sc2.png",width=150,height=210)
		sc3=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\sc3.png",width=150,height=210)
		sc4=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\sc4.png",width=150,height=230)

		fb1=Button(n1,image=sc1,command=p2.down)
		fb1.place(x=50,y=50)
		fb2=Button(n1,image=sc2,command=p2.down)
		fb2.place(x=220,y=50)
		fb3=Button(n1,image=sc3,command=p2.down)
		fb3.place(x=390,y=50)
		fb4=Button(n1,image=sc4,command=p2.down)
		fb4.place(x=560,y=50)
		
		#Horror
		l6=Label(n1,text=" Horror ",font='times_new_roman',bg='skyblue')
		l6.place(x=50,y=270)
		#i=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\logo.png",width=150)
		h1=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\h1.png",width=150,height=210)
		h2=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\h2.png",width=150,height=210)
		h3=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\h3.png",width=150,height=210)
		h4=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\h4.png",width=150,height=210)

		hb1=Button(n1,image=h1,command=p2.down)
		hb1.place(x=50,y=300)
		hb2=Button(n1,image=h2,command=p2.down)
		hb2.place(x=220,y=300)
		hb3=Button(n1,image=h3,command=p2.down)
		hb3.place(x=390,y=300)
		hb4=Button(n1,image=h4,command=p2.down)
		hb4.place(x=560,y=300)
		
		n1.mainloop()
		
	x=Toplevel()
	x.title("English Language")
	x.geometry("1400x1200")
	x.configure(bg='skyblue')
	l2=Label(x,text="English Novels....",font='times_new_roman',bg='lightgreen',fg='Red')
	l2.place(x=450,y=30)
	
	#Historical
	l6=Label(x,text=" Historical ",font='times_new_roman',bg='skyblue')
	l6.place(x=50,y=70)
	#i=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\logo.png",width=150)
	hi1=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\hi1.png",width=150,height=210)
	hi2=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\hi2.png",width=150,height=210)
	hi3=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\hi3.png",width=150,height=210)
	hi4=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\hi4.png",width=150,height=210)
	hib1=Button(x,image=hi1,command=p2.down)
	hib1.place(x=50,y=100)
	hib2=Button(x,image=hi2,command=p2.down)
	hib2.place(x=220,y=100)
	hib3=Button(x,image=hi3,command=p2.down)
	hib3.place(x=390,y=100)
	hib4=Button(x,image=hi4,command=p2.down)
	hib4.place(x=560,y=100)
	
	
	#Fictions
	l4=Label(x,text="fiction ",font='times_new_roman',bg='skyblue')
	l4.place(x=50,y=350)
	#i=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\logo.png",width=150)
	f1=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\f1.png",width=150,height=220)
	f2=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\f2.png",width=150,height=220)
	f3=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\f3.png",width=150,height=220)
	f4=PhotoImage(file="C:\\Users\\arunj\\OneDrive\\Pictures\\english\\f4.png",width=150,height=220)

	fb1=Button(x,image=f1,command=p2.down)
	fb1.place(x=50,y=380)
	fb2=Button(x,image=f2,command=p2.down)
	fb2.place(x=220,y=380)
	fb3=Button(x,image=f3,command=p2.down)
	fb3.place(x=390,y=380)
	fb4=Button(x,image=f4,command=p2.down)
	fb4.place(x=560,y=380)
	
	nb=Button(x,text="Next",command=nex)
	nb.place(x=100,y=700)
	
	
	
	x.mainloop()		
		
		


