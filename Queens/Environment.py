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
		self.stats = StatsModule(agents)

	def step(self):
		for t in self.tables:
			mes, new_state = t.agent.send(t.board)
			if isinstance(mes, str) and mes == "Success":
				self.stats.add_win(t)
				t.randomize_board(self.queens)
			elif isinstance(mes, str) and mes == "NoOp":
				self.stats.add_loss(t)
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
		while True:
			self.step()
			for t in self.tables:
				if len(self.stats.solutions[t.agent]) >= how_many:
					self.print_stats()
					return

	def print_stats(self):
		self.stats.print_stats(self.tables, self.queens)


class StatsModule:
	""" Class to measure agent's performance. Should be called on every win and loss which occurs
	in the environment. """
	def __init__(self, agents):
		self.count = len(agents)
		self.solutions = dict([(k, set()) for k in agents])
		self.win_times = dict([(k,[]) for k in agents])
		self.loss_times = dict([(k, []) for k in agents])
		
	def add_win(self, table):
		self.win_times[table.agent].append(table.perf)
		if not tuple(table.board.tolist()) in self.solutions:
			self.solutions[table.agent].add(tuple(table.board.tolist()))
	
	def add_loss(self, table):
		self.loss_times[table.agent].append(table.perf)
	
	def print_stats(self, tables, queens):
		for t in tables:
			# print("Agent with limit", t.agent.threshold)
			self.print_table_stats(t)

	def print_table_stats(self, table):
		win = len(self.win_times[table.agent])
		loss = len(self.loss_times[table.agent])
		print("Found {} solutions".format(len(self.solutions[table.agent])))
		if win + loss > 0:
			print("Win ratio:", win/(win + loss))
			print("Avg. win time:", np.average(self.win_times[table.agent]))
			print("Avg. loss time:", np.average(self.loss_times[table.agent]))
		
		
		
		
		
		
		
		