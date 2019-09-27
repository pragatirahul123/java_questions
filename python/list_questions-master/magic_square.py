magic_square =[[8,3,4],
                [1,5,9],
                [6,7,2]]
count=0
counter=-1
sum=0
store=0
while count<len(magic_square):
    sum=sum+magic_square[count][count]
    store=store+magic_square[counter][counter]
    count=count+1
    counter=counter-1
print sum
print store

