from Queens.Environment import QueensEnv
from Queens.Agents import *

queens = 8
k = 8

# plateauLimitedGenerator = PlateauLimitedAgent()
# stepGenerator = SteepestAscentAgent()
agents = [plateauLimitedGenerator(t) for t in range(k)]

a = steepestAscentAgent()
a.send(None)
env = QueensEnv(agents, queens=queens)

# env.find_sol(92)
env.find_sol(2)
# print(env.stats.solutions)
