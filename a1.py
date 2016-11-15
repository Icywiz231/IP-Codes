s=input("Enter sentence \n")
n=len(s)
ucase=0
lcase=0
for i in range(0,n):
	if(ord(s[i]) in range(65,90)):
		ucase+=1		
	if(ord(s[i]) in range(97,122)):
		lcase+=1		
print(ucase,lcase)
