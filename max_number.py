def maxnum(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
value=maxnum(12,65,100)
print value
