#this code seraches for an element in an unsorted list

l=[7,4,6,8,3,2,6,9]
inp=int(input("enter an element to be searched\n"))


def unsortedSearch(l,k):				#where k is the element to be searched	
		for i in range(len(l)):
			if l[i]==k:
				return i
		return "not found"	
o=unsortedSearch(l,inp)
print(o)





