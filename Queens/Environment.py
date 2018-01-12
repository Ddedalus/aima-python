import numpy as np

class Table:
	"""
	Simple storage class for single agent and it's board. Provides plotting utilities but does not
	tackle actions or agent messages. Also stores performance measure and random board generator.
	"""
	def __init__(self, agent, queens):
		self.board = self.randomize_board(queens)
		self.agent_func = agent
		self.perf = 0

	def randomize_board(self, queens):
		self.board = np.random.randint(0, queens - 1, queens)
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
	def __init__(self, agents, queens=8, boards=1, master_agents=[]):
		assert isinstance(agents, list)
		self.solutions = {}
		self.queens, self.boards = queens, boards
		self.random_state()
		self.tables = [Table(a, queens). for a in agents]
		for a, b in agents:
			a.performance = 0
		self.master_agents = master_agents

	
	def step(self):
		for pair in self.agents:
			a, b = pair
			mes, state = a(b)
			if mes == "Success":
				self.win_times.append(a.performance)
				a.performance = 0
				# self.solutions.add(b)
				pair[1] = self.random_state()

			elif a.performance >= int(0.5 * self.queens):
				b = self.random_state()
				a.performance = 0
			else:
				a.performance += 1
				b = state
	def execute_action(self, agent, action):
	
	
	def print_stats(self):
		print("Win ratio:", len(self.win_times) / (len(self.fail_times) + len(self.win_times)))
		print("Average fail time:", sum(self.fail_times) / len(self.fail_times))
		print("Average win time:", sum(self.win_times) / len(self.win_times))
	
	def __init__(self):
		self.things = []
		self.agents = []
	
	def thing_classes(self):
		return []  # List of classes that can go into environment
	
	def percept(self, agent):
		"""Return the percept that the agent sees at this point. (Implement this.)"""
		raise NotImplementedError
	
	def execute_action(self, agent, action):
		"""Change the world to reflect this action. (Implement this.)"""
		if action != "":
			raise NotImplementedError
	
	def default_location(self, thing):
		"""Default location to place a new thing with unspecified location."""
		return None
	
	def exogenous_change(self):
		"""If there is spontaneous change in the world, override this."""
		pass
	
	def is_done(self):
		"""By default, we're done when we can't find a live agent."""
		return not any(agent.is_alive() for agent in self.agents)
	
	def step(self):
		"""Run the environment for one time step. If the
		actions and exogenous changes are independent, this method will
		do. If there are interactions between them, you'll need to
		override this method."""
		if not self.is_done():
			actions = []
			for agent in self.agents:
				if agent.alive:
					actions.append(agent.program(self.percept(agent)))
				else:
					actions.append("")
			for (agent, action) in zip(self.agents, actions):
				self.execute_action(agent, action)
			self.exogenous_change()
	
	def run(self, steps=1000):
		"""Run the Environment for given number of time steps."""
		for step in range(steps):
			if self.is_done():
				return
			self.step()
	
	def list_things_at(self, location, tclass=Thing):
		"""Return all things exactly at a given location."""
		return [thing for thing in self.things
		        if thing.location == location and isinstance(thing, tclass)]
	
	def some_things_at(self, location, tclass=Thing):
		"""Return true if at least one of the things at location
		is an instance of class tclass (or a subclass)."""
		return self.list_things_at(location, tclass) != []
	
	def add_thing(self, thing, location=None):
		"""Add a thing to the environment, setting its location. For
		convenience, if thing is an agent program we make a new agent
		for it. (Shouldn't need to override this.)"""
		if not isinstance(thing, Thing):
			thing = Agent(thing)
		if thing in self.things:
			print("Can't add the same thing twice")
		else:
			thing.location = location if location is not None else self.default_location(thing)
			self.things.append(thing)
			if isinstance(thing, Agent):
				thing.performance = 0
				self.agents.append(thing)
	
	def delete_thing(self, thing):
		"""Remove a thing from the environment."""
		try:
			self.things.remove(thing)
		except ValueError as e:
			print(e)
			print("  in Environment delete_thing")
			print("  Thing to be removed: {} at {}".format(thing, thing.location))
			print("  from list: {}".format([(thing, thing.location) for thing in self.things]))
		if thing in self.agents:
			self.agents.remove(thing)
