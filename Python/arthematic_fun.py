#simple arthematics with python...


def my_function(fname):
	print("my_function param is "+ fname);

def sum(a, b):
	return a+b;

def oddeven(a):
	if(a%2 == 0):
		print(a," is even")
	else:
		print(" is odd")

def divisors(number):
	x = 1
	while x<= number:
		if number % x == 0 :
			print x
			x+=1
		else:
			x+=1


def cubes(n):
	return n **3;

lmbda = lambda x,y: x*y

fname = "hero";
my_function(fname);

print(sum(10,20));
print(cubes(4));
print(lmbda(2,7));
