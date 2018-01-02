from agents import *

def OurVacuum():
    Env = TrivialVacuumEnvironment()
    Env.add_things(TraceAgent(RandomVacuumAgent()))
    return Env
    Env.add_thing(TraceAgent(RandomVacuumAgent()))
