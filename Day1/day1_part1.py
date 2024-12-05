f = open("input.txt", "r")
list1 = []
list2 = []
sum = 0

line1 = f.readlines()

for line in line1:
    list1.append(line[0:5])
    list2.append(line[8:13])

list1 = sorted(list1)
list2 = sorted(list2)

for i in range(len(list1)):
    num1 = int(list1[i])
    num2 = int(list2[i])
    sum += abs(num1-num2)

print(sum)
f.close()