a=input("Enter First Number : ")
operator=input("Enter Operator (+,-,/,*) : ")
b=input("Enter Sceond Number : ")
int(a)
int(b)

if operator == "+" :
        print(a + b)
elif operator == "-" :
         print(a - b)
elif operator == "*" :
         print(a * b)
elif operator == "/" :
         print(a / b)
elif operator == "%" :
         print(a%b)   
else :
  print("Invalid Operation")
