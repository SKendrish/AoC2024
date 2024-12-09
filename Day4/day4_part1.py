import numpy as np
from collections import defaultdict

dirs = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

with open('input.txt', 'r') as f:
    data = f.readlines()
    keyword = 'XMAS'
    count = 0

    char_map = defaultdict(set)

    for r, row in enumerate(data):
        for c, val in enumerate(row):
            char_map[val].add((r,c))

    for r,c in char_map["X"]:
        for dr, dc in dirs:
            for i, char in enumerate(keyword[1:], 1):
                if (r + (dr*i), c + (dc*i)) not in char_map[char]:
                    break
            else:
                count+=1
    
    print(count)
