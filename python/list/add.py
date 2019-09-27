n=[10,11,12,13,14,17,18,19]
i=0
new=[]
while i<len(n):
    j=0
    while j<len(n):
    sum=sum(n[i]+[j]) 
  	if sum == 30:
     new.append(n[i],n[j])
    j=j+1
i=i+1    
