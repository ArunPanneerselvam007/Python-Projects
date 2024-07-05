#customer Details
def dtail():
	print("Customer Details")
	global a,b,c,d,e
	a=input("Name:")
	b=input("Address:")
	c=int(input("Pincode:"))
	d=input("Landmark:")
	e=int(input("Phone Number:"))
	return pay()
	
	
#Payment
def pay():
	print("Payment..?")
	print("1.Online Payment\n2.Cash On Delivery")
	global f
	f=int(input("Enter your choice:"))
	if f==1:
		global x,y
		x=int(input("Account Number:"))
		y=int(input("Pin:"))
		if x=='' and y=='':
			print("Enter Account No./Pin")
		else:
			print(conord())
	elif f==2:
		print(conord())
	else:
		print("Invalid Choice")
		print(pay())
	return ""
	
#Conform the Order
def conord():
	print("\n---Customer Details---")
	print("Name:",a)
	print("Address:",b)
	print("Pincode:",c)
	print("Landmark:",d)
	print("Phone Number:",e)
	if f==1:
		print("Account No:",x)
	
	
	z=input("Place Order [yes/No]:")
	if z=='yes':
		print("Order Placed SuccessFully")
		print("Thanks For Purchasing...")
		print("Have a happy day")
	else:
		print("Thanks For Visiting")
	return ""

	
def paycon():
	c=input("Buy Now[Yes/No]:")
	if c=='yes':
		print(dtail())
	else:
		print("Thanks for Visiting..")
	return exit
