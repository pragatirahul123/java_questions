my_file3 = open("file_question3.txt","w")
banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(banks_list):
	my_file3.write(banks_list[i]+"\n")
	i=i+1
my_file3.close()
















