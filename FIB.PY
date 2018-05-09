#this is the code for fibonacci without memoisation
def fib(x):
	if (x<=1):
		return x 						#this is the base case
	else:
		#print (fib(x-1)+fib(x-2))
		return (fib(x-1)+fib(x-2))		#this is the recursive case
	

term=fib(20)
print(term)

for i in range(20):
	print (fib(i))




