from Queens.Environment import QueensEnv
from Queens.Agents import *

queens = 8  # how big is the chessboard

env = QueensEnv([steepestAscentAgent()], queens=queens)
env.run(200)
# Let agent do 2000 steps and see how many solutions it finds

print()
steep = steepestAscentAgent()
plateau = plateauExplorerAgent()
env = QueensEnv([steep, plateau], queens=queens)
env.find_sol(73)
# challenge which agent finds 90% of all solutions possible

print()
agents = [plateauLimitedAgent(t) for t in range(6)]
env = QueensEnv(agents, queens=queens)
env.find_sol(73)
# see for how long is it efficient to explore the plateau

print()
agents = [steepestAscentAgent() for t in range(4)]
master = masterBeamAgent(queens)
env = QueensEnv(agents, master=master, queens=queens)
env.find_sol(73)
# use beam search to find all the solutions

# remember to check the plots ;)