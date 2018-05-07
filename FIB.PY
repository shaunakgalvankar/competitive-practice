#this is the code for fibonacci 
def fib(x):
	if (x<=1):
		return x
	else:
		#print (fib(x-1)+fib(x-2))
		return (fib(x-1)+fib(x-2))
	

term=fib(20)
print(term)

for i in range(20):
	print (fib(i))




