import numpy as np

def count_collisions(board):
	count = 0
	queens = len(board)
	for i in range(queens):
		for j in range(i + 1, queens):
			if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
				count += 1
	return count


def check_actions(board):
	queens = len(board)
	dt = np.dtype([('count', int), ('state', int, (queens,))])
	d = np.empty([queens, queens], dtype=dt)
	run = np.array(board)
	for q in range(queens):
		for i in range(queens):
			run[q] = i
			d[q, i] = (count_collisions(run), np.array(run))
		run[q] = board[q]
	
	ret = np.sort(d, axis=None, order='count')
	return ret