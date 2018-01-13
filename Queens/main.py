import numpy as np
from Environment import QueensEnv
from SteepestAscentAgent import SteepestAscentAgent

queens = 9
k = 8

agentGenerator = SteepestAscentAgent()
agent = agentGenerator.new_agent()
a2 = agentGenerator.new_agent()
env = QueensEnv([agent], queens=queens)

env.find_sol(400)

print(env.stats.solutions)
env.stats.printStats()
