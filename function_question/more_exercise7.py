list=["rishab","rishab","abhishek","diwakar","diwakar"]
index=0
new=[]
while index<len(list):
     if list[index]not in new:
         new.append(list[index])
     index=index+1
print new
