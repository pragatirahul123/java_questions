list1=[10,20,20,10,10,30,50,10,20,50,]
index=0
count=0
while index<len(list1):
        var=index+1
        while var<len(list1):
            if list1[index]==list1[var]:
		del(list1[index])
		count=count+1
		break
	    var=var+1
	index=index+1
print count
		
