f = open("input.txt", "r")

def conv_to_numlist(x):
    num_list = []

    for i in range(len(x)):
        report = x[i].split(' ')
        num_report = list(map(int,report))
        num_list.append(num_report)

    return num_list


reports = f.readlines()

numlist = conv_to_numlist(reports)
def numSafeReports(data):
    ans = 0
    for list in data:
        inc = 0
        dec = 0
        for i in range(0, len(list) - 1):
            first = list[i]
            second = list[i+1]
            lenList = len(list)
            #increasing
            if first < second and abs(first-second) <= 3 and first != second:
                inc += 1
            #decreasing
            if first > second and abs(first-second) <= 3 and first != second:
                dec += 1
            if inc == lenList - 1 or dec == lenList - 1:
                ans += 1
    return ans

print(numSafeReports(numlist))
f.close()