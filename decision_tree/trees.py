from math import log

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
        print item, prob
        shannonEnt -= prob * log(prob,2)
    return shannonEnt


def genDataSet():
    dataSet = [
                [1,1,'yes'],
                [1,1,'yes'],
                [1,0,'no'],
                [0,1,'no'],
                [0,1,'no']]
    return dataSet

def testCalcShannonEnt():
    dataSet = genDataSet()
    ent = calcShannonEnt(dataSet)
    print 'ShannonEnt:',ent

if __name__ == '__main__':
    testCalcShannonEnt()




