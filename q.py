def f123():
	yield 1
	yield 2
	yield 3
	
print(f123())

for i in f123():
	print(i)
