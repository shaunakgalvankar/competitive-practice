#this is the code for factorial of a number
def fact(x):
	if (x==1):
		return x    		#this establishes the base case for the recursion

	else:
		return x*fact(x-1)






l=fact(5)
print(l)