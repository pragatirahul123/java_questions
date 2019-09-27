def harshad_number(a):
	index=0
	sum=0
	a_digits=(str(a))
	print a_digits
	while index<len(a_digits):
    		sum=sum+int(a_digits[index])
    		index=index+1
	print sum
	if a%sum==0:
    		print"true"
	else:
    		print "false"
harshad_number(24)
