user=int(raw_input("enter a number"))
i=0
new=[]
while i<(user):
	user1=int(raw_input("enter a number"))
	new.append(user1)	
	i=i+1
print new
user2=int(raw_input("enter a number"))
if user2 in  new:
	print"list me  hai"
else:
	print" list me nhi  hai"
