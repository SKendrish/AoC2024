import re

pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

with open('input.txt', 'r') as f:
    data = f.read()

    ans = 0

    matches = pattern.finditer(data)

    for match in matches:
         ans += int(match.group(1))*int(match.group(2))

    print(ans)
        







