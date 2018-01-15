from Queens.Environment import QueensEnv
from Queens.Agents import *

queens = 8
k = 4

# plateauLimitedGenerator = PlateauLimitedAgent()
# stepGenerator = SteepestAscentAgent()
agents = [steepestAscentAgent() for t in range(k)]
master = masterBeamGenerator(queens)
env = QueensEnv(agents, master=master, queens=queens)


env.find_sol_master(40)
# env.run(400)
# env.print_stats()
# print(env.stats.solutions)
