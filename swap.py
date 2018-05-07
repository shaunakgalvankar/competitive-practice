#this is the module which can be used to swap two elements in a list using their indexes
#feel free to import 

def swap(a,b,l):
	temp=l[a]
	l[a]=l[b]
	l[b]=temp
	return l

l=[0,1,2,3,4,5,6,7,8,9,10]			#use this list to put in data to be swapped
#print(swap(7,8,l))					#uncomment this to see how this function works