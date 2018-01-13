from Environment import QueensEnv
from Agents import *

queens = 8
k = 8

# plateauLimitedGenerator = PlateauLimitedAgent()
# stepGenerator = SteepestAscentAgent()
agents = [plateauLimitedGenerator(t) for t in range(k)]
for a in agents: a.send(None)

a = steepestAscentAgent()
a.send(None)
env = QueensEnv([a], queens=queens)

# env.find_sol(92)
env.find_sol(20)
# print(env.stats.solutions)


