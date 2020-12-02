import csv
import random
import math
import operator
def loadDataSet(filename, split, trainingSet = [], testSet = []):
    with open(filename,'r')as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for i in range(len(dataset)-1):
            for j in range(4):
                dataset[i][j] = float(dataset[i][j])
            if random.random() < split:
                trainingSet.append(dataset[i])
            else:
                testSet.append(dataset[i])
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for i in range(length):
        distance += pow((instance1[i] - instance2[i]),2)
    return math.sqrt(distance)
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for i in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[i], length)
        distances.append((trainingSet[i], dist))
    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors
def getResponse(neighbors):
    classVotes = {}
    for i in range(len(neighbors)):
        response = neighbors[i][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key = operator.itemgetter(1), reverse = True)
    return sortedVotes[0][0]
def getAccuracy (testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] is predictions[i]:
            correct += 1
        result = (correct/float(len(testSet)))
    print(result)
    return result
def main():
    #Prepare Data
    trainingSet = []
    testSet = []
    split = 0.67
    loadDataSet(r'iris.csv', split, trainingSet, testSet)
    print('Train: ' + repr(len(trainingSet)))
    print('Test: ' + repr(len(testSet)))
    #generate Predictions
    predictions = []
    k = 3
    for i in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[i], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted = ' + repr(result) + ', actual = ' + repr(testSet[i][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
main()





