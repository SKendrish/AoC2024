import re

pattern1 = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
pattern2 = re.compile(r'do\(\)')
pattern3 = re.compile(r'don\'t\(\)')
muls = []

with open('input.txt', 'r') as f:
    data = f.read()

    #matches = pattern1.finditer(data)
    matchesDo = pattern2.finditer(data)
    matchesDont = pattern3.finditer(data)

    for match in matchesDo:
        print(match)

    # for match in matches:
    #     ans += int(match.group(1))*int(match.group(2))
        







