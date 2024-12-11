from collections import defaultdict
import re

def checkOrder(numList, int_map):
    badNum = 0
    for i in range(len(numList) - 1):
        copy = numList[i+1:]
        if numList[i] not in int_map[copy[0]]:
            isValid = True
            copy.pop(0)
        else:
            isValid = False
            badNum = numList[i]
            break
    return isValid, badNum

def getMiddleIndex(numList):
    return numList[int((len(numList) - 1) / 2)]

def sumMiddles(listONumLists, int_map):
    middle = 0
    for numList in listONumLists:
        if checkOrder(numList, int_map):
            middle += getMiddleIndex(numList)
    return middle


with open ('example.txt', 'r') as f:
    data = f.readlines()

    int_map = defaultdict(set)
    listOfNumList = []
    badListMap = defaultdict(list)
    fixedBadLists = []
    example = [61,13,29]

    for line in data:
        if '|' in line:
            int_map[int(line[0:2])].add(int(line[3:5]))
        if ',' in line:
            nums = re.findall(r'[0-9][0-9]', line)
            listOfNumList.append(list(map(int,nums)))

    for numList in listOfNumList:
        isValid = checkOrder(numList, int_map)[0]
        badNum = checkOrder(numList, int_map)[1]
        if not isValid:
            badListMap[badNum].append(numList)

    for key in badListMap.keys():
        for list in badListMap[key]:
            badNumIndex = list.index(key)
            goodList = list[0:badNumIndex]
            resofList = list[badNumIndex+1:]
            for i in range(len(resofList)):
                resofList.insert(i, key)
                if checkOrder(resofList, int_map)[0]:
                    goodList.append(resofList)
                    fixedBadLists.append(goodList)
                    break
                else:
                    resofList.remove(key)

    print(fixedBadLists)