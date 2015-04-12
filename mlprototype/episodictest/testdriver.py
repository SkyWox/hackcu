from scipy import *
import sys, time

from pybrain.rl.learners.valuebased import ActionValueNetwork
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q, SARSA, NFQ
from pybrain.rl.experiments.episodic import EpisodicExperiment
from pybrain.rl.environments import Task
from tasktest import TestTask
from envtest import TestEnv
from mlprototype.hackedexplorer import EpsilonHackedExplorer

env = TestEnv()
task = TestTask(env)

controller = ActionValueNetwork(1000, 3)
learner = NFQ()
learner = EpsilonHackedExplorer(env)
print "Explorer: " + str(learner.explorer)
agent = LearningAgent(controller, learner)
print "Explorer: " + str(learner.explorer)

experiment = EpisodicExperiment(task, agent)
print "Explorer: " + str(learner.explorer)

i = 0
while True:
    experiment.doEpisodes(1)
    print "Learning"
    agent.learn()
    agent.reset()
    i += 1
    print "Cycle: %d" %i
    if i > 60:
        agent.learning = False

