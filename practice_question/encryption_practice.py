list1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
user=raw_input("enter a alphabet")
index=0
while index<len(list1[index]):
    j=0
    while j<len(list1[j]):
        if user<list1[index][j]:
            j=j+2
        index=index+1
    print list1[index]
