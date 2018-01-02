from agents import *
def our_vacuum():
    env = TrivialVacuumEnvironment()
    env.add_thing(TraceAgent(RandomVacuumAgent()))
    return env
