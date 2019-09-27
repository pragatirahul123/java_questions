user=int(raw_input("enter a number"))
index=0
new=[]
count=0
while index<(user):
    user1=int(raw_input("enter a number"))
    new.append(user1)
    index=index+1
print new
if user1[index] < 0: 
	print "positive number",count
elif user[index]>l0:
	print"negative number",count      
elif user1[index] %2==0: 
 	print "even number",count	  
elif user1[index]%2!=0:
	print "odd number",count
elif user1[index]==0:
	print "zero",count
	count=count+1
index=index+1
		


