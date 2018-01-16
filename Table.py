import numpy as np


class Table:
	"""
	Simple storage class for single agent and it's board. Provides plotting utilities but does not
	tackle actions or agent messages. Also stores performance measure and random board generator.
	"""
	
	def __init__(self, agent, queens):
		self.perf = 0
		self.board = self.randomize_board(queens)
		self.agent = agent
		self.name = agent.send(None)
		self.message = ""
	
	def randomize_board(self, queens):
		self.board = np.random.randint(0, queens - 1, queens)
		self.perf = 0
		return self.board
	
	def plot_board(self):
		print("--" * (len(self.board) + 2))
		for row in self.board:
			print(str(row) + " " + "  " * row + "x")
		print("--" * (len(self.board) + 2))
	
	def print_board(self):
		print(self.board.tolist())
