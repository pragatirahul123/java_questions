list=[7,8,4,2,3,5,1,6]
i=0
while i<len(list):
  	j=0
	while j<len(list):
		if list[i]<list[j]:
			a=list[i]
			list[i]=list[j]
			list[j]=a
		j=j+1
	i=i+1
print list
		
