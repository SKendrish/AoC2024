import numpy as np


f = open("input.txt", "r")

def conv_to_numlist(x):
    num_list = []

    for i in range(len(x)):
        report = x[i].split(' ')
        num_report = list(map(int,report))
        num_list.append(num_report)

    return num_list

data = f.readlines()

numlist = conv_to_numlist(data)
example = [[7, 6, 4, 2, 1],
           [1, 2, 7, 8, 9],
           [9, 7, 6, 2, 1],
           [1, 3, 2, 4, 5],
           [8, 6, 4, 4, 1],
           [1, 3, 6, 7, 9]]
def isSafe(report):
    if len(report) <= 1:
        return True
    diffs = np.diff(report)
    isAsc = np.all(diffs >= 1) and np.all(diffs <= 3)
    isDesc = np.all(diffs >= -3) and np.all(diffs <= -1)
    if isAsc or isDesc:
        return True
    else:
        return False
                
def numSafeReports(reports):
    return sum(isSafe(report) for report in reports)

def checkBadReports(report):
    if not isSafe(report):
        for level in range(len(report)):
            if isSafe(np.delete(report, [level])):
                return True
        return False
    return isSafe(report)

def numSafeReports2(reports):
    return sum(checkBadReports(report) for report in reports)

print(numSafeReports2(numlist))

f.close()