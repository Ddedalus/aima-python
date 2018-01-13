import numpy as np
from Environment import QueensEnv
from PlateauExplorerAgent import PlateauExplorerAgent, PlateauLimitedAgent
from SteepestAscentAgent import SteepestAscentAgent

queens = 8
k = 8

plateauLimitedGenerator = PlateauLimitedAgent()
stepGenerator = SteepestAscentAgent()

env = QueensEnv(
	[PlateauLimitedAgent.new_agent(t) for t in range(1, k)],
                queens=queens)

# env.find_sol(92)
env.find_sol(20)
# print(env.stats.solutions)


