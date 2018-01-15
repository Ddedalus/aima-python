import numpy as np
import warnings


class StatsModule:
	""" Class to measure agent's performance. Should be called on every win and loss which occurs
	in the environment. Counts:
	 - ticks - how many times agents change state
	 - win and loss times - how many moves before Success/NoOp
	 - solutions - set of distinct solutions found by each agent
	"""
	
	def __init__(self, agents, master=None):
		self.count = len(agents)
		self.solutions = dict([(k, set()) for k in agents])
		if master:
			self.master = master
			self.solutions[master.agent] = set()
		else:
			self.master = None
		self.win_times = dict([(k, []) for k in agents])
		self.loss_times = dict([(k, []) for k in agents])
		self.steps, self.ticks = 0, 0

	def print_stats(self, tables):
		"""Main method to be called when testing is finished"""
		print("\nTotal steps:", self.steps)
		print()
		# master stats go first
		self.ticks += sum([t.perf for t in tables])
		
		print("Total ticks taken:", self.ticks)
		if self.master:
			print("{} found {} solutions using {} threads\n"
			      .format(self.master.name, len(self.solutions[self.master.agent]),
			              len(tables)))
		print()
		
		# table stats
		
		for t in sorted(tables, key=lambda tab: len(self.solutions[tab.agent]), reverse=True):
			with warnings.catch_warnings():
				warnings.simplefilter("ignore", category=RuntimeWarning)
				self.print_table_stats(t)

	def print_table_stats(self, table):
		win = len(self.win_times[table.agent])
		loss = len(self.loss_times[table.agent])
		print("Agent {} found {} solutions".format(table.name, len(self.solutions[table.agent])))
		if win + loss > 0:
			print("Win ratio:", win / (win + loss))
			print("Avg. win time:", np.mean(self.win_times[table.agent]))
			print("Avg. loss time:", np.mean(self.loss_times[table.agent]))
			print()

	def add_win(self, table):
		"""Called when agent reports winning combination as it's state. Returns the number of new
		solutions."""
		self.ticks += table.perf
		self.win_times[table.agent].append(table.perf)
		if not tuple(table.board.tolist()) in self.solutions:
			self.solutions[table.agent].add(tuple(table.board.tolist()))
			if self.master:
				self.solutions[self.master.agent] \
				.add((tuple(table.board.tolist())))
			return 1
		self.ticks += table.perf
		return 0
	
	def add_loss(self, table):
		"""Called when agent takes no further action"""
		self.loss_times[table.agent].append(table.perf)
		self.ticks += table.perf

