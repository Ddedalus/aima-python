from Queens.Table import Table
from Queens.Stats import StatsModule


class QueensEnv:
	""" Environment for all agents and boards. Here steps are evaluated, found solutions stored
	and performance measurement calls may be implemented. """
	def __init__(self, agents, queens=8, master=None):
		assert isinstance(agents, list)
		self.queens = queens
		self.tables = [Table(a, queens) for a in agents]
		self.master = [] if master is None else [Table(master, queens)]
		self.stats = StatsModule(agents, self.master[0])

	def step(self):
		for t in self.tables:
			t.message, new_state = t.agent.send(t.board)
			if isinstance(t.message, str) and t.message == "Success":
				self.stats.add_win(t)
				t.randomize_board(self.queens)
			elif isinstance(t.message, str) and t.message == "NoOp":
				self.stats.add_loss(t)
				t.randomize_board(self.queens)
			else:
				t.perf += 1
				t.board = new_state
		self.stats.steps += 1
		
		for su in self.master:
			su.agent.send(self.tables)

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
		self.stats.print_stats(self.tables)
