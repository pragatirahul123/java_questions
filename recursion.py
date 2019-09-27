def display(factorial):
	if (factorial == 0):
		return 1
	else:
		smallNum = (display(factorial-1))
		return factorial * smallNum
print(display(5))
		
