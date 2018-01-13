import numpy as np
from Environment import QueensEnv
from PlateauExplorerAgent import PlateauExplorerAgent
from SteepestAscentAgent import SteepestAscentAgent

queens = 8
k = 8

plateauGenerator = PlateauExplorerAgent()
stepGenerator = SteepestAscentAgent()

env = QueensEnv([plateauGenerator.new_agent()], queens=queens)
env2 = QueensEnv([stepGenerator.new_agent()], queens=queens)

# env.find_sol(92)
sol_no = []
for env in [env, env2]:
	env.find(85)
	# print(env.stats.solutions)
	env.stats.printStats()


