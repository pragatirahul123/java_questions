list1=[1,2,3,4,[5,3,4],6,5,9]
index=0
while index<len(list1):
    if type(list1[index])==list:
        var=0
        while var<len(list1[index]):
            print list1[index][var]
            var=var+1 
    index=index+1

