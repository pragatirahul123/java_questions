a=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
count =0
counter =0
var=0
while i<len(a):
	if a[i]>=10000000:
		count=count+1
	elif a[i] <= 100000:
		counter=counter+1
	else:
		var=var+1
	i = i + 1
print count,"crorepti"
print counter,"lakhpti"
print var,"dilwale"
