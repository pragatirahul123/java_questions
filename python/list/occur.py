a=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
new=[]
while i<len(a[i]):
	j=1
	count=0
	while j<len(a):
		if a[i]==a[j]:
			count=count+1
		j=j+1
	if [a[i],count] not in new:
		new.append ([a[i],count])
	i=i+1		
print new
