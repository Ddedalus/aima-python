from Agents import *

def OurVacuum():
    Env = TrivialVacuumEnvironment()
    Env.Add.Things(TraceAgent(RandomVacuumAgent()))
    return Env
