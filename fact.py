#this is the code for factorial of a number
def fact(x):
	if (x==1):
		return x    		#this establishes the base case for the recursion

	else:
		return x*fact(x-1)  #this is the recursive case


l=fact(5)					#this just catches the output of the function and stores it to a vaariable
print(l)