user=int(raw_input("enter a number"))
i=0
sum=0
var=0
while i<(user):
    user1=int(raw_input("enter a number"))
    if user1%2==0:
        sum=sum+user1
    else:
        var=var+user1
    i=i+1
print "sum of odd numbers",sum
print "sum of even numbers",var

