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


#получение прототипов
def get_prototypes(dataset, prototypes, iteration, prototypes_class, K):
    
    def get_class_of_obj(obj):
        return obj[len(obj)-1]

    def check_prototype(item, prototypes):
        for i in prototypes:
            if get_class_of_obj(item) == get_class_of_obj(i):
                return False
        return True

    if iteration == 0:
        count = 0
        while count < K:
            item = rnd.choice(dataset)
            if check_prototype(item, prototypes):
                prototypes.append(item)
                prototypes_class.append(item[len(item)-1])
                count += 1

#получение кластеров
def get_clasters(dataset, prototypes, clasters):
    for i in dataset:
        min = 10
        t = 0
        for j in range(len(prototypes)):
            d = evk(i, prototypes[j])
            if d < min:
                min = d
                t = j
        clasters[t].append(i)

#получение новых прототипов в кластерах
def get_new_prototype_of_claster(dataset, clasters, prototypes_class):
    def toFixed(numObj, digits=0):
        return f"{numObj:.{digits}f}"

    def get_prototype(claster, i):
        sum = []
        new_prot = []
        lenght_obj = len(claster[0])
        for i in range(lenght_obj):
            sum.append(0.0)
        for obj in claster:
            for i in range(lenght_obj-1):
                sum[i] += float(obj[i])
        for i in range(lenght_obj-1):
            new_prot.append(toFixed(sum[i]/len(claster), 1))
        return new_prot
    
    prototypes = []
    for i in range(len(clasters)):
        new_prot = get_prototype(clasters[i], i)
        new_prot.append(prototypes_class[i])
        prototypes.append(new_prot)
    return prototypes


#проверка на окончание цикла
def check_end(prot_prev, prot_new):
    for i in range(len(prot_new)):
        if prot_new[i] != prot_prev[i]:
            return True
    return False        

#метод К средних
def KMeansMethod(dataset):
    data = dataset.copy()
    data.remove(data[0])
    rnd.shuffle(data)
    K = 3
    S = 0
    clasters = []
    prototypes_prev = []
    prototypes_new = []
    prototypes_class = []
    for i in range(K):
        clasters.append([])
    f = True
    while (f):
        if S == 0:
            get_prototypes(data, prototypes_prev, S, prototypes_class, K)
        elif S != 0:
            get_clasters(data, prototypes_prev, clasters)
            prototypes_new = get_new_prototype_of_claster(data, clasters, prototypes_class)
            f = check_end(prototypes_prev, prototypes_new)
            if (f):
                prototypes_prev = prototypes_new
        S += 1
    
    for i in range(K):
        print()
        print(prototypes_new[i])
        print()
        print(clasters[i])


dataset = read_file("D:\Desktop\ПМИ\iris.csv")
KMeansMethod(dataset)