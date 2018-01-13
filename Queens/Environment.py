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
		self.queens = queens
		self.tables = [Table(a, queens) for a in agents]
		self.master_agents = master_agents
		self.stats = StatsModule(len(agents))

	def step(self):
		for t in self.tables:
			mes, new_state = t.agent(t.board)
			if isinstance(mes, str) and mes == "Success":
				self.stats.addWin(t)
				t.randomize_board(self.queens)
			elif isinstance(mes, str) and mes == "NoOp":
				self.stats.addLoss(t)
				t.randomize_board(self.queens)
			else:
				t.perf += 1
				t.board = new_state
		
		for su in self.master_agents:
			pass
		
	def run(self, steps):
		for i in range(steps):
			self.step()
			
	def find_sol(self, how_many):
		while len(self.stats.solutions)  < how_many:
			self.step()


class StatsModule:
	""" Class to measure agent's performance. Should be called on every win and loss which occurs
	in the environment. """
	def __init__(self, count):
		self.count = count
		self.solutions = set()
		self.win_times, self.loss_times = [], []
	
	def addWin(self, table):
		self.win_times.append(table.perf)
		if not tuple(table.board.tolist()) in self.solutions:
			self.solutions.add(tuple(table.board.tolist()))
			print(len(self.solutions))
	
	def addLoss(self, table):
		self.loss_times.append(table.perf)
	
	def printStats(self):
		total = len(self.win_times) + len(self.loss_times)
		print("Found {} solutions".format(len(self.solutions)))
		print("Win ratio:", len(self.win_times)/total)
		print("Avg. win time:", np.average(self.win_times))
		print("Avg. loss time:", np.average(self.loss_times))
