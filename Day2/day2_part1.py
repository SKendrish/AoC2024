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

print(reports)
f.close()