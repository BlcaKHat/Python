if __name__ == '__main__':
    n = int(raw_input())
    if n ==2 :
    	print 'Not Weird'
    elif (n %2 ==0 and n in range(5,20)) or (n%2 != 0 )	:
    	print "Weird"
    elif (n% 2 ==0 and n in range(1,5)) or (n % 2 ==0 and n > 20):
    	print 'Weird'
    else:
    	print 'not Weird' 