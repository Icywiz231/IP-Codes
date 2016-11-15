k=eval(input("Enter k"))

def lista(n):
	a=[]
	print("Enter list elements")
	for i in range(1,n+1):
		a.append(eval(input()))
	return(a)

n=eval(input("Enter n"))
l=lista(n)

def is_even_odd(n,k,l):
	i=0
	while(i<k):
		b=sum(l)
		l.append(b+1)
		i+=1
	if(l[-1]%2==0):
		return(l[-1])
	else:
		return(l[-1])

print(is_even_odd(n,k,l))
