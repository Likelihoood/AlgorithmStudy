#encoding=utf-8
from math import log
from draw_tree import *
'''
    calculate Shannon Entropy of the dataSet
'''
def calcShannonEnt(dataSet):
    totalNum = len(dataSet)
    disDic = {}
    for featureList in dataSet:
        item = featureList[-1]
        disDic.setdefault(item,0)
        disDic[item] += 1
    shannonEnt = 0.0
    for item in disDic:
        prob = disDic[item] / float(totalNum)
        shannonEnt -= prob * log(prob,2)
    return shannonEnt

'''
    split data set according to the value of the feature
'''
def splitDataSet(dataSet, axis, value):
    newSet = []
    for data in dataSet:
        if data[axis] == value:
            newFea = data[:axis]
            newFea.extend(data[axis+1:])
            newSet.append(newFea)
    return newSet
'''
    choose the best feature to split the data set
    find the highest information gain
    Iterative Dichotomiser 3 (ID3)
'''
def chooseBestFeatureToSplitByID3(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEnt = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeatureIndex = -1 
    for i in range(0,numFeatures):
        valueList = [featureVec[i] for featureVec in dataSet]
        valueSet = set(valueList)
        ent = 0.0
        for value in valueSet:
            subSet = splitDataSet(dataSet,i,value)
            newEnt = calcShannonEnt(subSet)
            newEnt = float(len(subSet)) / len(dataSet) * newEnt
            ent += newEnt
        infoGain = baseEnt - ent
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeatureIndex = i
    return bestFeatureIndex


def genDataSet():
    dataSet = [
                [1,1,'yes'],
                [1,1,'yes'],
                [1,0,'no'],
                [0,1,'no'],
                [0,1,'no']]
    labels = ['no surfacing','flippers']
    dataSet = [
            ['Sunny','Hot','High','Weak','No'],
            ['Sunny','Hot','High','Strong','No'],
            ['Overcast','Hot','High','Weak','Yes'],
            ['Rain','Mild','High','Weak','Yes'],
            ['Rain','Cool','Normal','Weak','Yes'],
            ['Rain','Cool','Normal','Strong','No'],
            ['Overcast','Cool','Normal','Strong','Yes'],
            ['Sunny','Mild','High','Weak','No'],
            ['Sunny','Cool','Normal','Weak','Yes'],
            ['Rain','Mild','Normal','Weak','Yes'],
            ['Sunny','Mild','Normal','Strong','Yes'],
            ['Overcast','Mild','High','Strong','Yes'],
            ['Overcast','Hot','Normal','Weak','Yes'],
            ['Rain','Mild','High','Strong','No']]
    labels = ['Outlook','Temperature','Humidity','Wind']
    return dataSet,labels

'''
    choose the lable which has the highest frequency
'''
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        classCount.setdefault(vote,0)
        classCount[vot] += 1
    soretedClassCount = sorted(classCount.items(),key=lambda item:item[1],reverse=True)

    return sortedClassCount[0][0]
'''
    create the tree recuried
'''
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet ]
    if classList.count(classList[0]) == len(classList): #if there is only one label in the classList
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    #split the dataset
    bestFeat = chooseBestFeatureToSplitByID3(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValue = [example[bestFeat] for example in dataSet]
    featValue = set(featValue)
    for value in featValue:
        subLabels = labels[:]
        subSet = splitDataSet(dataSet,bestFeat,value)
        myTree[bestFeatLabel][value] = createTree(subSet,subLabels)
    return myTree
'''
    classify
'''
def classify(dTree, labels, featureVec):
    firstLabel = dTree.keys()[0]
    
    firstIndex = labels.index(firstLabel)
    secondDic = dTree[firstLabel]
    for key in secondDic:
        if key == featureVec[firstIndex]:
            if type(secondDic[key]).__name__ == 'dict':
                return classify(secondDic[key],labels,featureVec)
            else:
                return secondDic[key]

def storeTree(dTree, filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(dTree,fw)
    fw.close()

def loadTree(filename):
    import pickle
    fr = open(filename)
    dTree = pickle.load(fr)
    return dTree


def testCalcShannonEnt():
    dataSet,labels = genDataSet()
    ent = calcShannonEnt(dataSet)
    print 'ShannonEnt:',ent

if __name__ == '__main__':
    dataSet,labels = genDataSet()
    
    myTree = createTree(dataSet,labels[:])
    print labels
    classify(myTree,labels,['Rain','Cool','Normal','Weak'])
    storeTree(myTree,'testFile.tree')
    dTree = loadTree('testFile.tree')
    print classify(dTree,labels,['Rain','Cool','Normal','Weak'])
    #createPlot(myTree)




