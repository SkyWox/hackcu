from scipy import *
import sys, time

from mlprototype.ravn import RestrictedActionValueNetwork
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners import Q, SARSA, NFQ
from pybrain.rl.experiments.episodic import EpisodicExperiment
from pybrain.rl.environments import Task
from mlprototype.episodictest.tasktest import TestTask
from mlprototype.episodictest.envtest import TestEnv
from mlprototype.hackedexplorer import EpsilonHackedExplorer

env = TestEnv()
task = TestTask(env)

controller = RestrictedActionValueNetwork(1000, 3, env)
learner = NFQ()
learner.explorer = EpsilonHackedExplorer(env)
agent = LearningAgent(controller, learner)

experiment = EpisodicExperiment(task, agent)

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

