import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
import random as rnd
import math as math
import csv

#считываем csv файл и конвертируем его в list
def read_file(inputfile):
    with open(inputfile, newline='') as f:
        reader = csv.reader(f)
        dataset = list(reader)
    return dataset

#метрика евклида
def evk(item1, item2):    
    return math.sqrt((float(item1[0])-float(item2[0]))**2 + (float(item1[1])-float(item2[1]))**2 +
                     (float(item1[2])-float(item2[2]))**2 + (float(item1[3])-float(item2[3]))**2)


#поиск расстояний
def get_prototype(item, data):
    max_dist = 0
    cur_data = 0
    for i in range(len(data)):
        cur_dist = evk(item, data[i])
        if cur_dist > max_dist:
            max_dist = cur_dist
            cur_data = i
    return cur_data


#среднее растояние между прототипами
def get_average_dist_of_prototype(prot):
    count = 0
    sum_dist = 0.0
    
    for i in range(len(prot)):
        for j in range(i+1, len(prot)):
            sum_dist += evk(prot[i], prot[j])
            count += 1       
        if count == 0:
            return 0.0
        return sum_dist / (2 * count)

#распределение объектов по кластерам
def get_clasters(prototypes, data):
    clasters = []
    d = []
    K = len(prototypes)
    for i in range(K):
        clasters.append([])
        d.append(0)
    t = 0
    for i in data:
        min = 10
        for j in range(K):
            d[j] = evk(i, prototypes[j])
        for k in range(len(d)):            
            if d[k] < min:
                min = d[k]
                t = k
        clasters[t].append(i)
    return clasters

#получение потенциального прототипа в своем кластере
def get_potential_prototype(prototypes, clasters, T, K):
    def get_obj_of_claster(claster, item ):
        return claster[item]
    f = True
    for i in range(K):
        y = get_prototype(prototypes[i], clasters[i])
        d = evk(prototypes[i], get_obj_of_claster(clasters[i], y))
        if d > T:
            f = False
            prototypes.append(get_obj_of_claster(clasters[i], y))
    return f
            

#метод максимина
def maksimin(dataset):
    data = dataset.copy()
    data.remove(data[0])
    #cur_data = rnd.randint(0, len(dataset)-10)
    cur_data = 18
    print(cur_data)
    K = 0
    prototypes = []
    prototypes.append(data[cur_data])
    p1 = get_prototype(prototypes[K], data)
    if p1 != cur_data:
        prototypes.append(data[p1])
        K = len(prototypes)
    
    f = False
    while(f == False):
        T = get_average_dist_of_prototype(prototypes)
        clasters = get_clasters(prototypes, data)
        f = get_potential_prototype(prototypes, clasters, T, K)
        
    K = len(prototypes)
    print(prototypes)
    print(K)
    print("End!")
    


dataset = read_file("D:\Desktop\ПМИ\iris.csv")
maksimin(dataset)

