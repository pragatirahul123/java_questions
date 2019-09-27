my_file = open("people1.exercise.txt","r")
file_data = my_file.readlines()
i=0
count=0
while i<len(file_data):
	count=count+1
	i=i+1
print count
my_file.close()

		








