list=[2,3,0,4,0,4,0,5,0,2]
index=0
new=[]
while index<len(list):
    if list[index]==0:
	new.append(list[index])
	list.remove(list[index])
    index=index+1
list.extend(new)
print list      
