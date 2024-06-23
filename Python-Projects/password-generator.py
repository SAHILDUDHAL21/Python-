#	CodSoft Internship (Python Programming)
#	Task 3
import random
import string

def pass_generate(l):
	char=string.ascii_letters+string.digits+string.punctuation
	passw="".join(random.choice(char)for _ in range(l))
	return passw

l=int(input("Enter Length of Password :: "))
passwd=pass_generate(l)
print("Generated Password :: ",passwd)