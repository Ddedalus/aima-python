from utility_measures import *

def steepestAscentAgent():
	state = yield
	while True:
		cols = count_collisions(state)
		if cols == 0:
			state = yield "Success", state
		else:
			update = check_actions(state)
			if update['count'][0] < cols:
				state = yield update, update['state'][0]
			else:
				state = yield "NoOp", state


def plateauExplorerGenerator():
	state = yield
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


def plateauLimitedGenerator(threshold):
	state = yield
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
