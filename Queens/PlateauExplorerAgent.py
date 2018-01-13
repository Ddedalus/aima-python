import numpy as np


class PlateauExplorerAgent:
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
			how_many = np.count_nonzero(ret['count'] == ret['count'][0])
			return ret[:how_many]
		
		def program(state):
			cols = count_collisions(state)
			if cols == 0:
				return "Success", state
			else:
				update = check_actions(state, 10)
				if update['count'][0] < cols:
					program.plateau = None
					return update, update['state'][0]
				elif program.plateau is None:   # we arrived to a plateau
					program.plateau = update[1:]
					return "Plateau", update['state'][0]
				elif len(program.plateau) > 0:  # there are options left to be explored
					ans = program.plateau['state'][0]
					program.plateau = program.plateau[1:]
					return "Plateau", ans
				else:   # explored plateau, nowhere to go
					return "NoOp", state
		
		return program
