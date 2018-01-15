from Queens.Environment import QueensEnv
from Queens.Agents import *

queens = 8
k = 8

# plateauLimitedGenerator = PlateauLimitedAgent()
# stepGenerator = SteepestAscentAgent()
agents = [steepestAscentAgent() for t in range(k)]
masters = [masterBeamGenerator(queens)]
env = QueensEnv(agents, master_agents=masters, queens=queens)

env.run(200)
env.print_stats()
# print(env.stats.solutions)
