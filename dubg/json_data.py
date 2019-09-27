import json
with open('users.json') as data_file:    
    data = json.load(data_file)
    #print type (data)
users = data["users"]
counter=0
while counter<len(users):
    print ("users full name is " + users[counter]['firstName'] + ' ' + users[counter]['lastName'])
    print ("users mobile number is " + str(users[counter]['details']['mobileNo']))
    print ("users age  is " + str(users[counter]['details']['age']))
    print ("users city is " + users[counter]['details']['City'])
    counter=counter+1
