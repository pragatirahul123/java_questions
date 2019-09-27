marks= [[78, 76, 94, 86, 88]
,[91,71,98,65,76],[95,45,78,52,49]]    
a =0
sum=0
new=[]
while a<len(marks):
    j=0
    while j<len(marks):
        sum=sum+marks[a][j]
        j=j+1
    new.append(sum)
    sum=0
    a=a+1
print new
    
