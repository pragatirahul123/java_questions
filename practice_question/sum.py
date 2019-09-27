list=[5,3,6,8,12,1]
largest=0
sum=0
var=0
while largest<len(list):
    sum=sum+list[largest] 
    largest=largest+1
while var<len(list):
    if largest < list[var]:
        largest=list[var]
    var=var+1
print largest
index=0
smallest=0
while index<len(list):
	smallest<list[index]
	smallest=list[index]
	index=index+1
print smallest	
print sum

