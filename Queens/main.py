import numpy as np
from importlib import reload
from Environment import QueensEnv
from SteepestAscentAgent import SteepestAscentAgent

queens = 8
k = 8

agentGenerator = SteepestAscentAgent()
agent = agentGenerator.new_agent()
a2 = agentGenerator.new_agent()
env = QueensEnv([agent])

env.run(200)