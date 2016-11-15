tup1=(1,2,3,4,5,6,7,8,9,10)
a=list(tup1)
a1=[]
for i in range(10):
	if(a[i]%2==0):
		a1.append(a[i])
tup2=tuple(a1)
print(tup2)
