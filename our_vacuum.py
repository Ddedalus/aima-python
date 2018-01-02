from agents import *

env = TrivialVacuumEnvironment()
env.add_thing(TraceAgent(RandomVacuumAgent()))
