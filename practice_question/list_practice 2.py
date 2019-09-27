list1=["pragati12@","hina21@","sapna10@","neha22@","ritu56@","komal11@"]
index=0
new=[]
while index<len(list1):
    var=0
    while var<len(list1):
        if list1[index] < list1[var] :
            del(list1[index])
            new.append(list1[var])
            var=var+1
        index=index+1
print list1

