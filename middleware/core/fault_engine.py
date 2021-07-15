#!/usr/local/bin python3

from middleware.src.dsl import mission
import random
import numpy as np
from deap import base
from deap import creator
from deap import tools
import matplotlib.pyplot as plt
from ..src.dsl.dslloader.mission_loader import MissionLoader
from ..src.dsl.dslloader.fault_specification import FaultSpecification
from ..src.dsl.dslloader.CI import CI


"""--------------------------------------------------------------------------------------------

                                      Genetic Algorithm

--------------------------------------------------------------------------------------------"""

def GA(NGEN, pop_size, INDPB, CXPB, evaluation_function):
    IND_SIZE = 100
    # Register the functions in the toolbox
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.uniform, -1.0, 1.0)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=IND_SIZE)

    toolbox.register("evaluate", evaluation_function)
    toolbox.register("select", tools.selRoulette)
    toolbox.register("mutate", tools.mutGaussian, mu=0.0, sigma=0.2, indpb=INDPB)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("mate", tools.cxOnePoint)

    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    logbook = tools.Logbook()
    pop = toolbox.population(pop_size)

    # Calculate the fitness of the initilised population
    fitnesses = [toolbox.evaluate(indiv) for indiv in pop]
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    for g in range(NGEN):
        print("-- Generation %i --" % g)

        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        # Crossover procedure
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        # Mutation procedure
        for mutant in offspring:
            toolbox.mutate(mutant)
            del mutant.fitness.values

        # Re-calcuate fitness after mutation and crossover
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = [toolbox.evaluate(indiv) for indiv in invalid_ind]
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # Insert into the previous population
        pop[:] = offspring
        record = stats.compile(pop)
        logbook.record(gen=g, **record)

    logbook.header = "gen", "avg", "evals", "std", "min", "max"

    gen = logbook.select("gen")
    avgs = logbook.select("avg")
    stds = logbook.select("std")
    mins = logbook.select("min")
    maxs = logbook.select("max")

    return [gen, avgs, stds, mins, maxs]

"""
-----------------------------------------------------------------------------------------------

                                        Utilities

-----------------------------------------------------------------------------------------------
"""
 # Setup mission specification
mission_loader = MissionLoader()
mission_specification = mission_loader.loadMission().mission

# Setup fault specification
fault_specification = FaultSpecification(mission)

# Setup CI
ci = CI(mission_specification, fault_specification)

# Fitness function
def evaluate(indiv):
    fitness = ci.runCI(indiv)
    return fitness,

# Plot statistics
def statistics():
    pass


"""--------------------------------------------------------------------------------------------

                                        Main

--------------------------------------------------------------------------------------------"""

def main():

    # Run GA
    global MAX
    global BEST
    generations = 4000
    population_size = 500
    MAX = 0
    BEST = []
    stats = GA(generations, population_size, 0.5, 0.4, evaluate)