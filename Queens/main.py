import numpy as np
from Environment import QueensEnv
from PlateauExplorerAgent import PlateauExplorerAgent
from SteepestAscentAgent import SteepestAscentAgent

queens = 8
k = 8

plateauGenerator = PlateauExplorerAgent()
stepGenerator = SteepestAscentAgent()

env = QueensEnv(
	[plateauGenerator.new_agent(), stepGenerator.new_agent()],
                queens=queens)

# env.find_sol(92)
env.find_sol(80)
# print(env.stats.solutions)


