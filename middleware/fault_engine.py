#!/usr/local/bin python3
import random
from deap.tools.support import ParetoFront
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
import sys

MAX = [{}, {}]
TYPE = ""
PARETO = []
goals = []
mission_duration = 0
# Setup CI
ci = CI()
mission_duration = ci.sim_interface.mission.duration
#ci.print_mission_and_fault_specification()
fs = FaultSpecification(MissionLoader().load_mission())

"""--------------------------------------------------------------------------------------------

                                      Genetic Algorithm

--------------------------------------------------------------------------------------------"""

def GA(NGEN, pop_size, mutate_prob, mate_prob):
    # Register the functions in the toolbox
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register("individual", tools.initIterate, creator.Individual, fs.generate_individual)
    toolbox.register("evaluate", evaluate)
    toolbox.register("select", tools.selRoulette)
    toolbox.register("mutate", mutate)
    toolbox.register("mate", mate)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    stats = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    logbook = tools.Logbook()
    pop = toolbox.population(pop_size)

    ci.sim_interface.MRS_init()
    time.sleep(4)
    
    if TYPE == '-mo': s ='mo'
    else : s ='so'
    # Calculate the fitness of the initilised population
    print("------------------------ Initilising Fitness -------------------------")
    with open(s + '_metrics.txt', 'a') as f:
        f.write("------------------------ Initilising Fitness -------------------------\n")
        f.close()
    fitnesses = [toolbox.evaluate(indiv) for indiv in pop]
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    #for ind, fit in zip(pop, fitnesses): print(ind, fit)

    for g in range(NGEN):
        print("---------------------------- Generation %i ----------------------------" % g)
        with open(s + '_metrics.txt', 'a') as f:
            f.write("---------------------------- Generation %i ----------------------------\n" % g)
            f.close()
        offspring = toolbox.select(pop, len(pop))
        offspring = list(map(toolbox.clone, offspring))

        # Crossover procedure
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < mate_prob:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        # Mutation procedure
        for mutant in offspring:
            if random.random() < mutate_prob:
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
def check_for_max(ci, fitness, indiv):
    global MAX
    sum_1, sum_2 = 0, 0
    for val in ci.goal_violations_per_goal.values(): sum_1 += val
    for val in MAX[1].values(): sum_2 += val
    if len(ci.goal_violations_per_goal) == len(MAX[1]):
        if sum_1 > sum_2: 
            MAX[0] = indiv
            MAX[1] = ci.goal_violations_per_goal
            print("New fault specification found! Fitness: {0} - Violations per Goal: {1} - ".format(fitness, ci.goal_violations_per_goal))
    elif len(ci.goal_violations_per_goal) > len(MAX[1]):
        MAX[0] = indiv
        MAX[1] = ci.goal_violations_per_goal
        print("New fault specification found! Fitness: {0} - Violations per Goal: {1} - ".format(fitness, ci.goal_violations_per_goal))

def pareto_front(ci):
    global PARETO
    flag = True
    p = []
    idv = [ci.goal_violations_per_goal[goals[0]], ci.goal_violations_per_goal[goals[1]]]
    p.append(idv[0])
    p.append(idv[1])
    temp_pareto = []
    if len(PARETO) == 0:
        PARETO.append(p)
    else:
        for i in PARETO:
            if (idv[0] <= i[0] and idv[1] <= i[1]):
                flag = False
                break
            elif (idv[0] >= i[0] and idv[1] >= i[1]):
                pass
            else:
                temp_pareto.append(i)
        if flag: 
            PARETO = temp_pareto
            PARETO.append(idv)
            print("New Pareto front found for Goals {0}, {1}: => {2}".format(goals[0], goals[1], PARETO))

# Fitness function
def evaluate(indiv):
    global TYPE
    global goals
    if TYPE == "-so": 
        fitness = ci.run_single_objective_CI(indiv)
        check_for_max(ci, fitness, indiv)    
    elif TYPE == "-mo": 
        fitness = ci.run_multi_objective_CI(indiv, goals)
        pareto_front(ci)
    return fitness,

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
        indiv[i].ft.mutate()
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
        f.close()
        plt.show(block=True)

"""--------------------------------------------------------------------------------------------

                                        Main

--------------------------------------------------------------------------------------------"""

if __name__ == "__main__":

    TYPE = sys.argv[1]
    if TYPE == '-mo':
        goals.append(sys.argv[2])
        goals.append(sys.argv[3])

    # Run GA
    generations = 50
    population_size = 20
    mutate_prob = 0.7
    mate_prob = 0.7
    statistics = GA(generations, population_size, mutate_prob, mate_prob)

    #print(MAX)

    if TYPE == '-mo':
        with open('mo_statistics.txt', 'w') as f:
            for stat in statistics:
                f.write(str(stat) + '\n')
            f.close()
    elif TYPE == '-so':
        with open('so_statistics.txt', 'w') as f:
            for stat in statistics:
                f.write(str(stat) + '\n')
            f.close()

    plt.xlabel('Generation')
    plt.ylabel('Mean Fitness')
    plt.scatter(statistics[0], statistics[1], label='Mean Fitness', color='blue')
    plt.yscale("log")
    plt.legend(loc='best', fancybox=True, framealpha=0.5)
    plt.show(block=True)

    plt.xlabel('Generation')
    plt.ylabel('Best Individual per generation')
    plt.scatter(statistics[0], statistics[4], label='Best Individual', color='blue')
    plt.yscale("log")
    plt.legend(loc='best', fancybox=True, framealpha=0.5)
    plt.show(block=True)