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


class QueensEnv:
	""" Environment for all agents and boards. Here steps are evaluated, found solutions stored
	and performance measurement calls may be implemented. """
	def __init__(self, agents, queens=8, master_agents=[]):
		assert isinstance(agents, list)
		self.solutions = {}
		self.queens = queens
		self.tables = [Table(a, queens) for a in agents]
		self.master_agents = master_agents
		self.stats = StatsModule(len(agents))

	def step(self):
		for t in self.tables:
			mes, new_state = t.agent(t.board)
			if mes == "Success":
				self.stats.addWin(t)
				# self.solutions.add(b)
				t.print_board()
				t.randomize_board()
			elif mes == "Pass":
				self.stats.addLoss(t)
				t.randomize_board()
			else:
				t.perf += 1
				t.board = new_state
		
		for su in self.master_agents:
			pass
		
	def run(self, steps):
		for i in range(steps):
			self.step()


class StatsModule:
	""" Class to measure agent's performance. Should be called on every win and loss which occurs
	in the environment. """
	def __init__(self, count):
		pass
	
	def addWin(self, Table):
		pass
	
	def addLost(self, Table):
		pass
	
	def printStats(self):
		pass
