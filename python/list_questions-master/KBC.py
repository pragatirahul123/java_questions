question_list=["(*)How many continents are there?",
		"(*)what is the capital of india?",
		"(*)NG me kon se course pdhaye jate hai?"]

first_option=["(1)four","(1)chandigardh","(1)software engineer"]

second_option=["(2)nine","(2)bhopal","(2)counselling"]

third_option =["(3)seven","(3)chennai","(3)toursim"]

four_option =["(4)eight","(4)delhi","(4)agriculture"]
answer_key=[3,4,1]

lifeline =[["(1)seven","(2)nine"],
["(1)bhopal","(2)delhi"],["(1)softaware engineer"],["(2)counselling"]]
	 
lifeline_key=[1,2,1]
index=0
while index<len(question_list):
	print question_list[index]
	print first_option[index]
	print second_option[index]
	print third_option[index]
	print four_option[index]
	a=int(raw_input("enter a number"))
	if answer_key[index]==a:
		print"congrats!apka ans right hai"
	elif a==5050:
		print question_list[index]
		print lifeline[index]

		user=int(raw_input("enter a answer"))
		if user==lifeline_key[index]:
			print"your win"
		else:
			print"apko game se bahr kr diya hai"
			break
		index=index+1


