def total(list1):
    index=0
    sum=0
    while index<len(list1):
        sum=sum+list1[index]
        index=index+1
    return sum
a=total([10,20,20,50])
print a

