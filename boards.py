def makeBoard(n, m):
	"""
	creates a board with n rows and m columns of Xs
	print out board as Xs
	"""
	board = []
	for i in range(n):
		board.append([])
		for j in range(m):
			board[i].append('X')
	return board
	
def printBoard(n, m):
	board = ""
	for row in makeBoard(n, m):
		board = board + " ".join(row) + "\n"
	return board

	
print printBoard(9,9)
	

