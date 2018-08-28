#assinment 3 
def ascendings(A):	 # For ascending
	if len(A) < 2:
		print ('true1')
		return True
	for i in range(len(A) - 1):
   	    if A[i] - A[i+1]>0:
        	print ('false')
        	return False
        	
	print ('true')
	return True
	
a=[7]
ascendings(a)
