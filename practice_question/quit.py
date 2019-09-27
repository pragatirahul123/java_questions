index=1
sum=0
user1=raw_input("enter number or quit")
while index<=(user1):
    if user1=="quit":
        break
    user1=int(user1)
    if index<=user1:
        sum=sum+index
    index=index+1
if(sum!=0):
	print sum


