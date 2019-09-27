board =["-","-","-",
	"-","-","-",
	"-","-","-"]
def display():
	print (board[0] +"|"+board[1]+"|"+board[2])
	print (board[3] +"|"+board[4]+"|"+board[5])
	print (board[6] +"|"+board[7]+"|"+board[8])
display()
def handle_turn():
	position=int(raw_input("enter a index 1-9: "))
	position=int(position )-1
	board[position]="x"
	display()
handle_turn()

	




	
