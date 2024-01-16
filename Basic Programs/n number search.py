n=int(input("Enter Limit"))

a=[]

for i in range(0,n):
    num=int(input("Enter Number"))
    a.append(num)
 

x=int(input("Enter Number to Search"))
if x in a:
    print("Number Found")
else:
    print("Number Not Found")




