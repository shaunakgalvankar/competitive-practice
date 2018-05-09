#this is a program that computes the gcd of two given numbers
#this code blocks excutes a simple way to compute the gcd of a given number
def gcd(m,n):
	fm=[]
	fn=[]
	fc=[]
	for i in range (1,m+1):
		if(m%i==0):
			fm.append(i)
	for i in range (1,n+1):
		if(n%i==0):
			fn.append(i)	
	print(fm,fn)	
	for i in fm:
		if i in fn:
			fc.append(i)
	print(fc)
	print("the gcd is "+str(fc[-1]))

def improvedGCD(m,n):
	cf=[]
	for i in range(1,min(m,n)+1):
		if(i%m)==0and(i%n)==0:
			cf.append(i)

	print("the gcd is "+str(cf[-1]))


improvedGCD(14,21)

