#	CodSoft Internship (Python Programming)
#	Task 2

while True:
	a=int(input("\nEnter First Number :: "))
	b=int(input("Enter Second Number :: "))
	print("\n1 :: Addition \n2 :: Subtraction\n3 :: Multiplication\n4 :: Division")
	sw=int(input("\nEnter Choice :: "))
	print("\n")
	if(sw==1):
		print("Addition of ",a,"&",b,"is",a+b)
	elif(sw==2):
		print("Subtraction of",a,"&",b,"is",a-b)
	elif(sw==3):
		print("Multiplication of",a,"&",b,"is",a*b)
	elif(sw==4):
		print("Division of",a,"&",b,"is",a/b)
		print("Reminder of",a,"Divide by",b,"is",a%b)