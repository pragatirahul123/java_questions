def leap_year(year):
    index=0
    while index<year:
        if year%4==0:
            print "leap year",user1
        else:
            print"not leap year",user1
        index=index+1
        break
user1=int(raw_input("enter a number"))
leap_year(user1)
