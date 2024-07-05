"""==================================================================================
******PUTHAGACHOZHAI Online Shopping******
			#Ennidhaii Karpom Arram Payilvom """
print(__doc__)
import file1 as f1
print("==================================================================================")
print("\nWelcome to Puthagachozhai online book shopping")
def lan():
	print("Which language did you Prefer")
	print("1.Tamil\n2.English\n3.Others")
	l=int(input("Enter your choice:"))
	if l==1:
		f1.tamil()
	elif l==2:
		f1.english()
	elif l==3:
		f1.others()
	else:
		print("Invalid Option")
	return ""
		
print(lan())




	

	


