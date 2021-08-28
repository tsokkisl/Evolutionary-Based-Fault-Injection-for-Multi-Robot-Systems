#!/usr/local/bin python3
import random
import numpy as np
from deap import base
from deap import creator
from deap import tools
import matplotlib.pyplot as plt
from gen.mission_loader import MissionLoader
from gen.fault_specification import FaultSpecification
from gen.CI import CI
import time
import matplotlib.pyplot as plt
import ast

mission_duration = 0

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

# Fitness function
def evaluate(indiv):
    fitness = ci.runCI(indiv)
    return fitness,

# Plot statistics
def statistics():
    pass

def mutate(indiv):
    """print("indiv Before")
    print([[i.ft.message.ID, i.start, i.finish] for i in indiv])"""
    indiv.sort(key=lambda x : x.finish)
    for i in range(len(indiv)):
        # Find lower_bound
        j = i - 1
        while j >= 0 and indiv[j].ft.message.ID != indiv[i].ft.message.ID:
                j -= 1
        if j == -1:
            lower_bound = 0
        else:
            lower_bound = indiv[j].finish + 1
        j = i + 1
        # Find upper_bound
        while j < len(indiv) and indiv[j].ft.message.ID != indiv[i].ft.message.ID:
                j += 1
        if j == len(indiv):
            upper_bound = mission_duration
        else:
            upper_bound = indiv[j].start - 1
        indiv[i].start = random.randint(lower_bound, indiv[i].finish)
        indiv[i].finish = random.randint(indiv[i].start, upper_bound)
    """print("indiv After")
    print([[i.ft.message.ID, i.start, i.finish] for i in indiv])
    print("-----------------------------------------------------")"""

def is_valid_for_mate(f, l):
    flag = True
    for e in l:
        if (f.finish < e.start) or (f.start > e.finish):
            continue
        else:
            flag = False
            break
    return flag


def mate(indiv_1, indiv_2):
    """print("indiv Before")
    print([[i.ft.message.ID, i.start, i.finish] for i in indiv_1])
    print([[i.ft.message.ID, i.start, i.finish] for i in indiv_2])"""
    tmp_1, tmp_2 = [], []
    l1, l2 = len(indiv_1), len(indiv_2)
    for _ in range(l1):
        f = indiv_1.pop()
        if is_valid_for_mate(f, indiv_2):
            tmp_1.append(f)
        else:
            indiv_1.append(f)
        if len(tmp_1) >= len(indiv_1) // 2:
            break

    for _ in range(l2):
        f = indiv_2.pop()
        if is_valid_for_mate(f, indiv_1):
            tmp_2.append(f)
        else:
            indiv_2.append(f)
        if len(tmp_2) >= len(indiv_2) // 2:
            break
    indiv_1 += tmp_2
    indiv_2 += tmp_1
    """print("indiv After")
    print([[i.ft.message.ID, i.start, i.finish] for i in indiv_1])
    print([[i.ft.message.ID, i.start, i.finish] for i in indiv_2])
    print(tmp_1)
    print(tmp_2)
    print("-----------------------------------------------------")"""
    return indiv_1, indiv_2

def generate_plots():
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'pink', 'purple']
    i = 0
    with open('metrics.txt', 'r') as f:
        for line in f.readlines():
            l = []
            for val in sorted(ast.literal_eval(line).items(), key=lambda item: item[0]):
                l.append(int(val[1]))
            for _ in range(6 - len(l)): l.append(0)
            plt.plot(["g1", "g2", "g3", "g4", "g5", "g6"], l, color=colors[i], marker='.', linestyle = 'None', markersize = 12)
            i += 1
        plt.show(block=True)

"""--------------------------------------------------------------------------------------------

                                        Main

--------------------------------------------------------------------------------------------"""
# Setup CI
ci = CI()
mission_duration = ci.mission.duration
#ci.print_mission_and_fault_specification()

if __name__ == "__main__":
    pop = FaultSpecification(MissionLoader().load_mission()).generate_population(10)
    for i in range(1):
        print('---------------- Generation {0} ---------------'.format(i))
        for indiv in pop:
            if random.randint(0, 2) == 0:
                mutate(indiv)
        for indiv_1 in pop:
            for indiv_2 in pop:
                if random.randint(0, 2) == 0:
                    mate(indiv_1, indiv_2)
        ci.sim_interface.MRS_init()
        time.sleep(2)
        for indin in pop:
            ci.runCI(indiv)
            ci.sim_interface.reset()
            ci.sim_interface.mrs.reset()
    ci.sim_interface.mrs.kill()
    ci.sim_interface.kill()
    
    generate_plots()
    """# Run GA
    global MAX
    global BEST
    generations = 4000
    population_size = 500
    MAX = 0
    BEST = []
    stats = GA(generations, population_size, 0.5, 0.4, evaluate)"""