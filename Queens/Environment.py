from Queens.Table import Table
from Queens.Stats import StatsModule


class QueensEnv:
	
	"""Environment for all agents and boards. Here steps are evaluated
	and performance measurement calls occur.
	- agents - list of generators taking state and returning their move each step
	- master - optional master agent which can read everybody's messages and then arbitrarily
	change state of the tables. It is meant to be 'main thread' in multi thread algorithms like
	beam search"""
	def __init__(self, agents, queens=8, master=None):
		assert isinstance(agents, list)
		self.queens = queens
		self.tables = [Table(a, queens) for a in agents]
		if master:
			self.master = Table(master, queens)
		self.stats = StatsModule(agents, self.master)

	def step(self):
		""" This is a single iteration of search. Every agent returns message and new state.
			Then the master agent is called"""
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
		
		if self.master:
			self.master.agent.send(self.tables)

	def run(self, steps):
		"""Shorthand to run multiple steps"""
		for i in range(steps):
			self.step()

	def find_sol(self, how_many):
		"""Run until specified amount of distinct solutions is found by one of agents. May be
		used to compare performance in terms of steps/ticks"""
		while True:
			self.step()
			for t in self.tables:
				if len(self.stats.solutions[t.agent]) >= how_many:
					self.print_stats()
					return
				
	def find_sol_master(self, how_many):
		"""The same as above but all found solutions are on account of master agent"""
		while len(self.stats.solutions[self.master.agent]) < how_many:
			self.step()
		self.print_stats()

	def print_stats(self):
		self.stats.print_stats(self.tables)
