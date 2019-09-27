def even_function(num):
    index=0
    while index<len(num):
        if num[index]%2==0:
            print"even number",num[index]
        else:
            print"odd number",num[index]
        index=index+1
even_function([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
