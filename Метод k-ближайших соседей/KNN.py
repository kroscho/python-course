import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
import random as rnd
import math as math
import csv

K = 31

# считываем csv файл и конвертируем его в list
def read_file(inputfile):
    with open(inputfile, newline='') as f:
        reader = csv.reader(f)
        dataset = list(reader)
    return dataset

# метрика евклида
def evk(item1, item2):    
    return math.sqrt((float(item1[0])-float(item2[0]))**2 + (float(item1[1])-float(item2[1]))**2 +
                     (float(item1[2])-float(item2[2]))**2 + (float(item1[3])-float(item2[3]))**2)

# разделение мнодества на обучающую и тестовую выборки
def split_file(dataset):
    test_data = []
    train_data = dataset.copy()
    train_data.remove(train_data[0])
    N = int(len(dataset)*1/10)
    #print("N = ", N)
    rnd.shuffle(train_data)
    for i in range(N):
        test_data.append(train_data[0])
        train_data.remove(train_data[0])   
    return test_data, train_data

# вывод результата на экран
def printResult(resultList):
    for i in resultList:
        print(i)

# метод K ближайших соседей
def KNN(test_data, train_data):
    # получаем индекс класса объекта
    def getIndexClass(item):
        classType = item[4]
        if classType == "setosa":
            return 0
        elif classType == "versicolor":
            return 1
        elif classType == "virginica":
            return 2

    # определяем к какому классу относится объект
    def getIndexResultClass(classesDist):
        max = 0
        indexClass = 0
        for i in range(len(classesDist)):
            if classesDist[i] > max:
                max = classesDist[i]
                indexClass = i
        #print("setosa = ", classesDist[0], "   versicolor = ", classesDist[1], "   virginica = ", classesDist[2])
        if indexClass == 0:
            return "setosa"
        if indexClass == 1:
            return "versicolor"
        if indexClass == 2:
            return "virginica"
    
    # проверка правильности работы метода
    def checkResultList(resultList):
        t = 0
        for item in resultList:
            if item[0][4] == item[1]:
                t += 1
        result = t / len(resultList) * 100
        print("True classifier: ", result, "%")            

    resultList = []

    for testItem in test_data:
        testDist = []
        for j in range(len(train_data)):
            testDist.append([evk(testItem, train_data[j]), train_data[j]])
        testDist.sort()
        classesDist = [0, 0, 0]
        for i in range(K):
            indexClass = getIndexClass(testDist[i][1])
            if testDist[i][0] != 0.0:
                classesDist[indexClass] += 1 / testDist[i][0]
        resultClass = getIndexResultClass(classesDist)
        #print(testItem, "result_class = ", resultClass)
        resultList.append([testItem, resultClass])
    
    checkResultList(resultList)
    return resultList


dataset = read_file("D:\Desktop\ПМИ\iris.csv")
test_data, train_data = split_file(dataset)
resultList = KNN(test_data, train_data)
printResult(resultList)
