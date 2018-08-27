def greeting(name):
	print("hello, "+ name);

def addnumbers(a, b):
	c = a+b;
	return c;

def oddeven(a):
	if(a%2 == 0):
		print(a," is even")
	else:
		print(" is odd")

def divisors(number):
	#divs=[]
	x = 1
	while x<= number:
		if number % x == 0 :
			print x
			x+=1
		else:
			x+=1


	#print divs