list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
index=0
new=[]
while index<len(list1):
	j=0
	while j<len(list2):
		if list1[index] not in new:
			new.append(list1[index])
		if list2[j] not in new:
			new.append(list2[j])
		j=j+1

	index=index+1
print new
