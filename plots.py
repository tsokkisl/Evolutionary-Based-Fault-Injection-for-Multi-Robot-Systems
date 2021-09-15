from os import stat
import matplotlib.pyplot as plt
import ast
import random
import math

def pareto_plots():
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'orange', 'lime', 'purple']
    markers = ['x', '.', 'o', '^', '+']
    with open('middleware/mo_metrics.txt', 'r') as f:
        t1 = []
        t2 = []
        for line in f.readlines():
            l = line[:len(line) - 1].split(',')
            t1.append(float(l[0]))
            t2.append(float(l[1]))
        plt.plot(t1[1:21], t2[1:21], c='b', marker='o', label='generation 1', linestyle = 'None')
        plt.plot(t1[310:330], t2[310:330], c='yellow', marker='o', label='generation 15', linestyle = 'None')
        plt.plot(t1[639:659], t2[639:659], c='g', marker='^', label='generation 32', linestyle = 'None')
        plt.plot(t1[869:889], t2[869:889], c='orange', marker='x', label='generation 44', linestyle = 'None')
        f.close()
        plt.legend(loc='best', fancybox=True, framealpha=0.5)
        plt.xlabel('g1: Avoid Collision violations')
        plt.ylabel('g3: Sufficient Energy violations')
        plt.show(block=True)


    data1 = [5430, 2188, 1435, 1585, 365, 362, 258]
    data2 = [1125, 3311, 5080, 4533, 5491, 5916, 6449]
    plt.scatter(data1, data2, c='green')
    plt.xlabel('g1: Avoid Collision violations')
    plt.ylabel('g3: Sufficient Energy violations')
    plt.show(block=True)

def ga_statistics(type):
    statistics = []

    with open('middleware/'+ type +'_statistics.txt', 'r') as f:
        for line in f.readlines():
            statistics.append(ast.literal_eval(line))


    plt.xlabel('Generation')
    plt.ylabel('Mean Fitness')
    plt.scatter(statistics[0], statistics[1], color='green')
    plt.show(block=True)

    plt.xlabel('Generation')
    plt.ylabel('Maximum Fitness')
    plt.scatter(statistics[0], statistics[4], color='green')
    plt.show(block=True)

def bar_plot():
    statistics = []
    with open('middleware/so_metrics.txt', 'r') as f:
        for line in f.readlines():
            if line[0] != '-':
                line = ast.literal_eval(line)
                fs = []
                for k in range(len(line) - 2):
                    temp = line[k]
                    fs.append(temp["Type"])
                statistics.append([fs, line[len(line) - 1]])
    #print(statistics)
    statistics.sort(key=lambda x: x[1], reverse=True)
    statistics = statistics[0:10]
    result = {}
    for s in statistics:
        for i in s[0]:
            if i in result.keys():
                result[i] += 1
            else:
                result[i] = 1
    print(result)
    plt.ylabel('Occurrence')
    for k, v in result.items():
        rgb = (random.random(), random.random(), random.random())
        plt.bar(k, v, color=rgb)
        plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show(block=True)

#ga_statistics('mo')
pareto_plots()
#bar_plot()