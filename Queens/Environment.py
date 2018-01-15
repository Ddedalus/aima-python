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
			progress_bar(i, steps, "steps done.")

	def find_sol(self, how_many):
		"""Run until specified amount of distinct solutions is found by one of agents. May be
		used to compare performance in terms of steps/ticks"""
		max_found = 0
		while max_found < how_many:
			self.step()
			max_found = max(self.stats.solutions.values())
			progress_bar(max_found, how_many, "solutions found")
		self.print_stats()

	def find_sol_master(self, how_many):
		"""The same as above but all found solutions are on account of master agent"""
		found = 0
		while found < how_many:
			self.step()
			found = len(self.stats.solutions[self.master.agent])
			progress_bar(found, how_many, "solutions found by master")
		self.print_stats()

	def print_stats(self):
		self.stats.print_stats(self.tables)


def progress_bar(current, total, what):
	print('\r', current, "out of", total, what, end="", flush=True)
