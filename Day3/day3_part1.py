import re

pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

with open('input.txt', 'r') as f:
    data = f.read()

    ans = 0

    matches = pattern.findall(data)

    for match in matches:
         ans += int(match[0])*int(match[1])

    print(ans)
        







