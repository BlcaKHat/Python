import mymodule
from mymodule import addnumbers

#	mymodule.greeting("vijay");
# a = int(input("Enter the value of A"))
# b = int(input("Enter the value of B"))
# d = addnumbers(a,b);
# print(d);
# print(mymodule.oddeven(int(a)))

# f = open("esytst.txt", "r");
# print(f.read())

#num_arry = list()
#print(type(num_arry)) 
#num = input("Enter the number of inputs")
# for x in range(int(num)):
# 	n = input()
# 	num_arry.append(int(n))

# print num_arry

#mymodule.divisors(20)
# l1 = [1,2,3,4,5,2,5,3,5,6,7,8]
# l2 = [2,4,6,7,9,1,5,6,7,8,2,3,4,5,6,6]
# l3 = []
# print(len(l1))

# for x in range(0,(len(l1))):
# 	for y in range(0,(len(l2))):
# 		if l1[x] == l2[y]:
# 			l3.append(l1[x])

# print list(set(l3))
l1 = raw_input("Enter a String  ")
l2 = l1[::-1]
if str(l1) == str(l2):
	print("palandrome")
else:
	print("not palandrome")

