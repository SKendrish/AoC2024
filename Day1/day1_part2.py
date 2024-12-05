f = open("input.txt", "r")
list1 = []
list2 = []
simularity_score = 0

line1 = f.readlines()

for line in line1:
    list1.append(line[0:5])
    list2.append(line[8:13])

list1 = sorted(list1)
list2 = sorted(list2)

for i in range(len(list1)):
    count = list2.count(list1[i])
    simularity_score += int(list1[i])*count

print(simularity_score)
f.close()