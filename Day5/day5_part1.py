from collections import defaultdict
import re

def checkOrder(numList, int_map):
    for i in range(len(numList) - 1):
        copy = numList[i+1:]
        if numList[i] not in int_map[copy[0]]:
            isValid = True
            copy.pop(0)
        else:
            isValid = False
            break
    return isValid

def getMiddleIndex(numList):
    return numList[int((len(numList) - 1) / 2)]

def sumMiddles(listONumLists, int_map):
    middle = 0
    for numList in listONumLists:
        if checkOrder(numList, int_map):
            middle += getMiddleIndex(numList)
    return middle


with open ('input.txt', 'r') as f:
    data = f.readlines()

    int_map = defaultdict(set)
    listOfNumList = []

    for line in data:
        if '|' in line:
            int_map[int(line[0:2])].add(int(line[3:5]))
        if ',' in line:
            nums = re.findall(r'[0-9][0-9]', line)
            listOfNumList.append(list(map(int,nums)))

    print(sumMiddles(listOfNumList, int_map))
