import agents
from agents import *

from random import random
class VacuumEnvironment213(agents.TrivialVacuumEnvironment):
    def percept(self, agent):
        if random() < 0.9:
            return super().percept(agent)
        else:
            print("Dirt sensor failed")
            if self.status[agent.location] == "Dirty":
                return (agent.location, "Clean")
            else:
                return (agent.location, "Dirty")

    def execute_action(self, agent, action):
        if action is not "Suck" or random() < 0.75:
            # everything is normal
            super().execute_action(agent, action)
        else: # Suck failed
            print("Suck failed")
            if self.status[agent.location] == "Clean":
                print("Deposited dirt on a clean floor")
                self.add_thing(Dirt(), agent.location)

env = VacuumEnvironment213()
env.add_thing(agents.TraceAgent(agents.RandomVacuumAgent()))
env.run(100)


def OurVacuum():
    Env = TrivialVacuumEnvironment()
    Env.add_thing(TraceAgent(RandomVacuumAgent()))
    return Env
