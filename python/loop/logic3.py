a=[10,20,30],[40,50,60]
index=-1
new=[]
while index>=-len(a):
	new.extend(a[index])
	index=index-1
print new
