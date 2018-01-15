from Queens.Environment import QueensEnv
from Queens.Agents import *

queens = 8  # how big is the

# plateauLimitedGenerator = PlateauLimitedAgent()
# stepGenerator = SteepestAscentAgent()
agents = [steepestAscentAgent() for t in range(4)]
master = masterBeamGenerator(queens)
env = QueensEnv(agents, master=master, queens=queens)


env.find_sol_master(82)
# env.find_sol(10)
# env.run(400)
# env.print_stats()
# print(env.stats.solutions)

