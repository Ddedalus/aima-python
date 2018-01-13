import numpy as np


class SteepestAscentAgent:
	@staticmethod
	def new_agent():
		def count_collisions(board):
			count = 0
			queens = len(board)
			for i in range(queens):
				for j in range(i + 1, queens):
					if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
						count += 1
			return count
		
		def check_actions(board, how_many):
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
			return ret[:how_many]
		
		def program(state):
			cols = count_collisions(state)
			if cols == 0:
				return "Success", state
			else:
				update = check_actions(state, 10)
				if update['count'][0] < cols:
					return update, update['state'][0]
				else:
					return "NoOp", state
		
		return program
