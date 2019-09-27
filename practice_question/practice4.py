list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
index=0
new=[]
while index<len(list):
    if index<5:
         new.append(list[index])
    index=index+1
print new 
print list
user=int(raw_input("enter a number"))
var=0
new1=[]
while var<len(list):
    if user>list[var]:
        new1.append(list[var])
    var=var+1
print new1


