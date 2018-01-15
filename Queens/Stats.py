import numpy as np
import warnings


class StatsModule:
	""" Class to measure agent's performance. Should be called on every win and loss which occurs
	in the environment. """
	
	def __init__(self, agents, master):
		self.master_tab = master
		self.count = len(agents)
		self.solutions = dict([(k, set()) for k in agents])
		self.win_times = dict([(k, []) for k in agents])
		self.loss_times = dict([(k, []) for k in agents])
		self.steps = 0
	
	def add_win(self, table):
		self.win_times[table.agent].append(table.perf)
		if not tuple(table.board.tolist()) in self.solutions:
			self.solutions[table.agent].add(tuple(table.board.tolist()))
	
	def add_loss(self, table):
		self.loss_times[table.agent].append(table.perf)
	
	def print_stats(self, tables):
		print("\nTotal steps:", self.steps)
		print()
		# master stats go first
		
		sols = set().union(*self.solutions.values())
		ticks = sum([t.perf for t in tables])
		for win in self.win_times.values():
			ticks += sum(win)
		for loss in self.loss_times.values():
			ticks += sum(loss)
		print("Total ticks taken:", ticks);
		print("{} found {} solutions using {} threads\n"
		      .format(self.master_tab.name, len(sols), len(tables)))
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
