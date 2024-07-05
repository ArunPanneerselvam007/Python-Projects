import pymysql as my
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def dis():
	def d2():
		messagebox.showinfo("Download","Downloaded Successfully...!")
	
	d=Toplevel()
	d.title("Download Page")
	d.geometry("500x500")
	l1=Label(d,text="Click Here To Download")
	l1.place(x=200,y=200)
	b=Button(d,text='Download',bg='lightgreen',fg='magenta',command=d2)
	b.place(x=250,y=250)
	d.mainloop()
	
	
def down():
	t=Toplevel()
	t.title("Login Page")
	t.geometry("700x700")
	t.configure(bg='skyblue')
	l1=Label(t,text="Use your account for download",font='Algerian',bg='magenta',fg='yellow')
	l1.place(x='180',y='10')

	db=my.connect(host='localhost',user='root',password='',db='pythondb')
	cur=db.cursor()
	def login():
		cur.execute("select * from signup")
		x=e.get()
		y=e1.get()
		b=x,y
		if x=='' and y=='':
			messagebox.showinfo("Submit","Enter the Username/Password")
		else:
			for i in cur.fetchall():
				if b[0:2]==i[2:4]:
					messagebox.showinfo("Submit","Login Successfully...")
					dis()
					break
			else:
				messagebox.showerror("Submit","Invalid Username and Password")
		return ""

	def signup():
		cur.execute("select * from signup")	
		a=e2.get()
		b=e3.get()
		c=e4.get()
		d=e5.get()
		x=a,b,c,d
		if a=='' and b=='' and c=='' and d=='':
			messagebox.showinfo("Submit","Enter the details")
		else:
			for i in cur.fetchall():
				if x[1]==i[1] or x[2]==i[2] or x[3]==i[3]:		
					messagebox.showwarning("Submit","Data already Exist...")
					break
			else:
				cur.execute("insert into signup values('"+a+"','"+b+"','"+c+"','"+d+"')")
				messagebox.showinfo("Submit","Record Stored.....")
				db.commit()
				dis()
		return ""
	
	
	def clear():
		e.delete(0,'end')
		e1.delete(0,'end')
		e2.delete(0,'end')
		e3.delete(0,'end')
		e4.delete(0,'end')
		e5.delete(0,'end')
		return ""


	#login 
	l2=Label(t,text="For Login",font='Algerian',bg='magenta',fg='yellow')
	l2.place(x='20',y='100')
	l3=Label(t,text="username :",font='roman',bg='pink',fg='Black')
	l3.place(x='30',y='150')
	e=Entry(t,width='30')
	e.place(x='150',y='150')
	l4=Label(t,text="Password :",font='roman',bg='pink',fg='Black')
	l4.place(x='30',y='200')
	e1=Entry(t,width='30')
	e1.place(x='150',y='200')
	b1=Button(t,text="Submit",command=login)
	b1.place(x=30,y=240)
	b3=Button(t,text="Clear",command=clear)
	b3.place(x=100,y=240)

	#Signup
	l5=Label(t,text="For signup",font='Algerian',bg='magenta',fg='yellow')
	l5.place(x='20',y='300')
	l6=Label(t,text="Name:",font='roman',bg='pink',fg='Black')
	l6.place(x='30',y='350')
	e2=Entry(t,width='30')
	e2.place(x='180',y='350')
	l7=Label(t,text="Phone Number :",font='roman',bg='pink',fg='Black')
	l7.place(x='10',y='400')
	e3=Entry(t,width='30')
	e3.place(x='180',y='400')
	l8=Label(t,text="Username:",font='roman',bg='pink',fg='Black')
	l8.place(x='20',y='450')
	e4=Entry(t,width='30')
	e4.place(x='180',y='450')
	l9=Label(t,text="Password :",font='roman',bg='pink',fg='Black')
	l9.place(x='20',y='500')
	e5=Entry(t,width='30')
	e5.place(x='180',y='500')
	b1=Button(t,text="Submit",command=signup)
	b1.place(x=30,y=540)
	b3=Button(t,text="Clear",command=clear)
	b3.place(x=100,y=540)
	t.mainloop()
	return ""

