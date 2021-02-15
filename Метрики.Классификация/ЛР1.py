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

#метрика Хэмминга
def hamming(item1, item2):
    dist = 0
    for i in range(len(item1)-1):
        if item1[i] != item2[i]:
            dist += 1
    return dist

#метрика Манхэттэна
def manhattan(item1, item2):
    sum = 0
    for i in range(len(item1)-1):
        sum += math.fabs(float(item1[i])-float(item2[i]))
    return sum

#метрика Жаккара
#(отношение количества уникальных символов в двух множествах
#(букв в словах) к общему числу уникальных символов в двух множествах (словах))
def jacuard(item1, item2):
    return 1 - ((len(item1)-1)-hamming(item1, item2))/(len(item1)-1)

#косинусная метрика
#(скалярное произведение, деленное на длину каждого из двух векторов)
def cosine(item1, item2):
    def product(item1, item2):
        d = 0.0
        for i in range(len(item1)-1):
            d += float(item1[i])*float(item2[i])
        return d
    return 1 - product(item1, item2) / (math.sqrt(product(item1, item1)) * math.sqrt(product(item2, item2)))


#классификатор
def classifier_evk(test_data, train_data):
    #возврат тип вектора
    def type_vec(item):
        return item[4]
    x = "y"
    while x == "y":
        print("Выберите метрику:\n1-Евклида\n2-Хэмминга\n3-Городских кварталов\n4-Жаккарда\n5-Косинусная\n")
        metrika = int(input())
        type_item = type_vec(train_data[0])
        for i in test_data:
            min_distance = 10
            for j in train_data:
                if metrika == 1:
                    cur_dist = evk(i, j)
                elif metrika == 2:
                    cur_dist = hamming(i, j)
                elif metrika == 3:
                    cur_dist = manhattan(i, j)
                elif metrika == 4:
                    cur_dist = jacuard(i, j)
                elif metrika == 5:
                    cur_dist = cosine(i, j)
                else:
                    print("Вы ввели неверно, попробуйте еще раз!")
                    cur_dist = 0
                    x = "n"
                    break
                if (cur_dist < min_distance and x == "y"):
                    min_distance = cur_dist
                    type_item = type_vec(j)
                    jj = j
            if x == "y":
                print(i, "    res=  ", jj, "   res_type = ", type_item, "  dist = ", min_distance)
            else:
                break
        print("Вы хотите продолжить? y/n")
        x = input()

#делим датасет на обучающую и тестовую выборку
def split_file(dataset):
    test_data = []
    train_data = dataset.copy()
    train_data.remove(train_data[0])
    N = int(len(dataset)*1/10)
    print("N = ", N)
    rnd.shuffle(train_data)        #перетасовка строк случайным образом
    for i in range(N):
        test_data.append(train_data[0])
        train_data.remove(train_data[0])    
    classifier_evk(test_data, train_data)  

dataset = read_file("D:\Desktop\ПМИ\iris.csv")
split_file(dataset)

