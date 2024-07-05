import file2 as f2
import webbrowser as wb
#Joners
def tamil():
	print("Which Joner do you like?")
	print("1.Fiction\n2.Science Fiction\n3.Historical\n4.Horror")
	j=int(input("Enter your choice:"))
	if j==1:
		print(at1())
	elif j==2:
		print(at2())
	elif j==3:
		print(at3())
	elif j==4:
		print(at4())
	else:
		print("Invalid Choice")
		print(tamil())
	return ""
	
def english():
	print("Which Joner do you like?")
	print("1.Fiction\n2.Science Fiction\n3.Historical\n4.Horror")
	j=int(input("Enter your choice:"))
	if j==1:
		print(ae1())
	elif j==2:
		print(ae2())
	elif j==3:
		print(ae3())
	elif j==4:
		print(ae4())
	else:
		print("Invalid Choice")
		print(english())
	return ""
		
def others():
	print("Some of other language Novels")
	print("1.Mahaprastanam in Telugu\n2.Pathummayude Aadu\n3.Malegalali Madumagalu")
	o=int(input("Enter your choice:"))
	if o==1:
		print(wb.open_new_tab("https://www.goodreads.com/book/show/8493614-maha-prasthanam?ref=nav_sb_ss_1_4"))
	elif o==2:
		print(wb.open_new_tab("https://www.goodreads.com/book/show/12516807-pathummayude-aadu?ref=nav_sb_ss_1_7"))
	elif o==3:
		print(wb.open_new_tab("https://www.goodreads.com/book/show/11554723-malegalali-madumagalu?ref=nav_sb_ss_1_8"))
	else:
		print("Invaid Choice")
		print(others())
	return ""
	
#Authors for Tamil

def at1():
	print("Authors for Fiction")
	print("1.Kalki\n2.Sujatha\n")
	t1=int(input("Enter your choice:"))
	if t1==1:
		f2.tfk()
	elif t1==2:
		f2.tfs()
	else:
		print("Invaid choice")
		print(at1())
	return ""
	
def at2():
	print("Authors for Science Fiction")
	print("1.Era Natrasan\n2.Sujatha\n")
	t1=int(input("Enter your choice:"))
	if t1==1:
		f2.tse()
	elif t1==2:
		f2.tss()
	else:
		print("Invaid choice")
		print(at2())
	return ""
	
def at3():
	print("Authors for Historical")
	print("1.Kalki\n2.Jeyamohan\n")
	t1=int(input("Enter your choice:"))
	if t1==1:
		f2.thk()
	elif t1==2:
		f2.thj()
	else:
		print("Invaid choice")
		print(at3())
	return ""
		
def at4():
	print("Authors for Horror")
	print("1.Soundraya\n2.Karthik Selva\n")
	t1=int(input("Enter your choice:"))
	if t1==1:
		f2.tps()
	elif t1==2:
		f2.tpk()
	else:
		print("Invaid choice")
		print(at4())
	return ""
		
#Authors for English

def ae1():
	print("Authors for Fiction")
	print("1.Leo Tolstoy\n2.J K Rowling\n")
	t1=int(input("Enter your choice:"))
	if t1==1:
		f2.efl()
	elif t1==2:
		f2.efr()
	else:
		print("Invaid choice")
		print(ae1())
	return ""
		
def ae2():
	print("Authors for Science Fiction")
	print("1.H.G.Wells\n2.Aurthur C.Clarke\n")
	t1=int(input("Enter your choice:"))
	if t1==1:
		f2.esw()
	elif t1==2:
		f2.esa()
	else:
		print("Invaid choice")
		print(ae2())
	return ""
		
def ae3():
	print("Authors for Historical")
	print("1.Jane Auston\n2.Hillary Mantel\n")
	t1=int(input("Enter your choice:"))
	if t1==1:
		f2.ehj()
	elif t1==2:
		f2.ehh()
	else:
		print("Invaid choice")
		print(ae3())
	return ""
		
def ae4():
	print("Authors for Horror")
	print("1.Stephen King\n2.Clive Barker\n")
	t1=int(input("Enter your choice:"))
	if t1==1:
		f2.eps()
	elif t1==2:
		f2.epc()
	else:
		print("Invaid choice")
		print(ae4())
	return ""	
		
		
		
		
	
	
