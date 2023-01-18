'''
--[ Tic tac toe game to run in the command line ]--
written by Substing.

Notes:
*code is not orthogonal -a lot is hard coded
*output could potentially overwrite, and just have one board that changes... using "\r"
*if the user inputs a taken space, it does nothing
*if user puts in invalid, it just throws error, perhaps adding error handling is a good idea
'''



#libraries
import random

#functions
def display_board(board):
	#accepts board and prints
	print("")
	print("==========================")
	print('\n\n'.join(['\t'.join([str(cell) for cell in row]) for row in board]))
	print("==========================")
	print("")


def enter_move(board):
	#takes board, asks user input. 
	#Checks input , updates board
	move = int(input("> "))
	for i in range(3):
		for j in range(3):
			if board[i][j] == move:
				board[i][j] = "O"
	return board

def make_list_of_free_fields(board):
	#bulds list of free squares
	#list of tuples, (row, column)
	free = []
	for i in range(3):
		for j in range(3):
			if isinstance(board[i][j], int):
				free.append((i, j))
	return free
				


def victory_for(board, sign):
	#check if X or O has won by looking through board
	#winning cases
	'''

	whole row : if all of board[r][i] is the same - where i is variable
	whole column : if all of board[i][c] is the same - where i is variable
	diagonal : if board[i][j] is the same - where i == j 
				or if board[2][0], board[1][1], board[0][2] 

	'''
	#whole row
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2] == sign:
			return True
	
	#whole column 
	for i in range(3):
		if board[0][i] == board[1][i] == board[2][i] == sign:
			return True

	#first diagonal [0,0], [1,1], [2,2]
	if board[0][0] == board[1][1] == board[2][2] == sign:		
		return True

	#second diagonal [0,2] [1,1] [2,0]
	if board[0][2] == board[1][1] == board[2][0] == sign:		
		return True

	return False


def draw_move(board):
	#computer's random move
	free = make_list_of_free_fields(board)
	move = random.choice(free)
	board[move[0]][move[1]] = "X"
	return board

def main():

	board = [[1, 2, 3],
			[4, 5, 6],
			[7, 8, 9]]	

	while True:
		#computer moves
		draw_move(board)
		#check if x won
		if victory_for(board, "X") == True:
			print("X wins!")
			display_board(board)
			return
		#show board
		display_board(board)

		if len(make_list_of_free_fields(board)) == 0:
			print("Stalemate!")
			exit()

		#get input
		enter_move(board)

		display_board(board)

		#check if o won
		if victory_for(board, "O") == True:
			print("O wins!")				
			display_board(board)
			return

main()