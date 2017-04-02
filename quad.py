import os
import random
from datetime import datetime
import math
from copy import copy
from time import sleep


class quadwalker:


genome = []
best_genome = []
cur_fitness = 0
best_fitness = 0
iteration = 0

genome = initgenome()

def Getgenome():
  return self.genome

def Getbest_genome():
    return self.best_genome

def Getfitness():
    return self.cur_fitness

def Getbest_fitness():
    return self.best_fitness

def evaluate():
    cur_fitness = fit_func();
    generation += 1;

    if ( not best_genome ):
        add_best_indivisual()
    else if (cur_fitness > best_fitness && genome !=best_genome):
        add_best_indivisual()
        genome = best_genome[0]
    else:
        genome != best_genome

    genome = mutate()
    return genome

def fitness(x,y,z):
    return Math.sqrt(Math.pow(x,2)+Math.pow(y,2)+Math.pow(z,2))

def add_best_individual():
    best_genome = genome.slice();
    best_genomes.push(best_genome);
    best_fitness = cur_fitness;
    return 0
