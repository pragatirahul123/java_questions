def greatest(a,b,c):
    if (a>b and b>c):
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=input("enter a number")
b=input("enter a number")
c=input("enter a number")
v= greatest(a,b,c)
print v


