import json
with open('users.json','r') as data_file: 
	da = data_file.read()   
	data = json.loads(da)

users = data['users']

for user in data:
	counter = 0
	print "users full name is " + users['firstName'] + ' ' + users['lastName']
	while counter < len(users['details']):
		print "users mobile number is " + users['details'][counter]['mobileNo']
		print "users age  is " + users['details'][counter]['age']
		print "users city is " + users['details'][counter]['city']
		counter=counter+1

