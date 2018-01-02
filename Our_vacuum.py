from agents import *

def OurVacuum():
    Env = TrivialVacuumEnvironment()
    Env.add_thing(TraceAgent(RandomVacuumAgent()))
    return Env #dupa
