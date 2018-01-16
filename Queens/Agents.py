from Queens.utility_measures import *


def steepestAscentAgent():
	state = yield "steepestAscentAgent"
	while True:
		cols = count_collisions(state)
		if cols == 0:
			state = yield "Success", state
		else:
			update = check_actions(state)
			if update['count'][0] < cols:
				state = yield update[:len(state)], update['state'][0]
			else:
				state = yield "NoOp", state


def plateauExplorerAgent():
	state = yield "plateauExplorerAgent"
	plateau = None
	while True:
		cols = count_collisions(state)
		if cols == 0:
			state = yield "Success", state
		else:
			update = check_actions(state)
			if update['count'][0] < cols:
				plateau = None
				state = yield update, update['state'][0]
			elif plateau is None:  # we arrived to a plateau
				how_many = np.count_nonzero(update['count'] == update['count'][0])
				plateau = update[1:how_many]
				state = yield "Plateau", update['state'][0]
			
			elif len(plateau) > 0:  # there are options left to be explored
				state = yield "Plateau", plateau['state'][0]
				plateau = plateau[1:]
			else:  # explored plateau, nowhere to go
				state = yield "NoOp", state


def plateauLimitedAgent(threshold):
	state = yield "PlateauLimited, max={}".format(threshold)
	plateau, count = None, 0
	while True:
		cols = count_collisions(state)
		if cols == 0:
			state = yield "Success", state
		else:
			update = check_actions(state)
			if update['count'][0] < cols:
				plateau, count = None, 0
				state = yield update, update['state'][0]
			
			elif plateau is None:  # we arrived to a plateau
				how_many = np.count_nonzero(update['count'] == update['count'][0])
				plateau = update[1:how_many]
				count += 1
				state = yield "Plateau", update['state'][0]
			
			elif len(plateau) > 0 and count < threshold:  # there are options left to
				#  be explored
				ans = plateau['state'][0]
				plateau = plateau[1:]
				count += 1
				state = yield "Plateau", ans
			
			else:  # explored plateau or time over, nowhere to go
				state = yield "NoOp", state


def masterBeamAgent(queens):
	tables = yield "Master Beam Generator"
	k = len(tables)
	while True:
		av = np.empty(0, dtype=dt(queens))
		for t in tables:
			if not isinstance(t.message, str):
				av = np.unique(np.concatenate((av[:k], t.message)))
				av.sort(kind='mergesort')
				t.message = None
		
		for t, s in zip(tables, av):
			if not isinstance(t.message, str):
				t.state = s['state']
		tables = yield
