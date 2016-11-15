a=eval(input("Enter a"))
b=eval(input("Enter b"))
c=eval(input("Enter c"))
d=eval(input("Enter d"))
def get_special_numbers(a,b,c,d):
	a1=[]
	print("Enter list elements")
	for i in range(c,d+1):
		if(i%a==0 and i%b!=0):
			a1.append(i)
	print(a1)
get_special_numbers(a,b,c,d)
