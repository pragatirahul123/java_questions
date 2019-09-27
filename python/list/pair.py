n=[10,11,12,13,14,17,18,19]
i=0
sum=0
new=[]
while i<len(n):
    j=i+1
    while j<len(n):
        sum=n[i]+n[j]
        if sum==30:
                new.append([n[i],n[j]])
        j=j+1
    i=i+1
print new
