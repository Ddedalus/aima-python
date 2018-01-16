import numpy as np


def dt(queens):
	"""numpy data type used to store (collision count, board state) pair"""
	return np.dtype([('count', int), ('state', int, (queens,))])


def count_collisions(board):
	"""Count how many pairs of queens are checking each other"""
	count = 0
	queens = len(board)
	for i in range(queens):
		for j in range(i + 1, queens):
			if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
				count += 1
	return count


def check_actions(board):
	"""What are the values of utility function for all possible moves? This function expands the
	given node and returns list of it's descendants sorted by utility"""
	queens = len(board)
	d = np.empty([queens, queens], dtype=dt(queens))
	run = np.array(board)
	for q in range(queens):
		for i in range(queens):
			run[q] = i
			d[q, i] = (count_collisions(run), np.array(run))
		run[q] = board[q]
	
	ret = np.sort(d, axis=None, order='count')
	return ret