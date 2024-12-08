import re

pattern1 = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
pattern2 = re.compile(r'do\(\)(.*)don\'t\(\)')
pattern3 = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))")
muls = []

with open('input.txt', 'r') as f:
    data = f.read()

    #matches = pattern2.finditer(data)
    matches = pattern3.findall(data)

    ans = 0
    do = True

    for i in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", data):
        match i:
            case "do()":
                do = True
            case "don't()":
                do = False
            case _:
                x, y = map(int, i[4:-1].split(','))
                if do:
                    ans += x*y   
    print(ans)

        







