import random
import numpy as np
import time
from models import Para
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", np.ndarray, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

def subject_time_check(para, subject_time):
    neg = [0 if assign_time.studyTime > sub_time else (sub_time - assign_time.studyTime) for assign_time, sub_time in zip(para.test_list, subject_time)]
    return sum(neg) * -1 * para.sizeLow

def evalOneMax(individual, para):
    value_weight = np.array([x * y for x, y in zip(individual, para.weight)])
    value_weight_array = value_weight.reshape(para.sizeLow, para.sizeCol)
    individual_array = individual.reshape(para.sizeLow, para.sizeCol)
    subject_time = np.sum(individual_array, axis=0)
    negativ = subject_time_check(para, subject_time)

    for ind, val_wei in zip(individual_array, value_weight_array):
        if sum(ind) > para.sizeCol:
            negativ = negativ - (sum(val_wei) / 2)
    return sum(value_weight) + negativ,

def cxTwoPointCopy(ind1, ind2):
    size = len(ind1)
    cxpoint1 = random.randint(1, size)
    cxpoint2 = random.randint(1, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else: # Swap the two cx points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

    ind1[cxpoint1:cxpoint2], ind2[cxpoint1:cxpoint2] = ind2[cxpoint1:cxpoint2].copy(), ind1[cxpoint1:cxpoint2].copy()

    return ind1, ind2

def main(para):
    random.seed(time.time())

    toolbox.register("attr_bool", random.randint, 0, 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=para.size)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", evalOneMax, para=para)
    toolbox.register("mate", cxTwoPointCopy)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)


    pop = toolbox.population(n=100)
    hof = tools.HallOfFame(1, similar=np.array_equal)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats,halloffame=hof)

    return hof
