user=raw_input("enter a password")
if len(user)>=6 and len(user)<=16:
    if "$" > user:
        if "2" or "8"> user:
            if "A" or "Z"> user:
                print"strong password"
else:
    	print "weak password"
