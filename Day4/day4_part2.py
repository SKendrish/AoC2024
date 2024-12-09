import numpy as np
from collections import defaultdict

dirs = [(-1,-1), (-1, 1), (1,-1), (1,1)]

upleft = lambda r, c: (r-1, c-1)
upright = lambda r, c: (r-1, c+1)
downleft = lambda r, c: (r+1, c-1)
downright = lambda r, c: (r+1, c+1)

with open('input.txt', 'r') as f:
    data = f.readlines()
    count = 0

    char_map = defaultdict(set)

    for r, row in enumerate(data):
        for c, val in enumerate(row):
            char_map[val].add((r,c))

    for r, c in char_map["A"]:
            if upleft(r,c) in char_map["M"]:
                 if upright(r,c) in char_map["M"] and downleft(r,c) in char_map["S"] and downright(r,c) in char_map["S"]:
                    count += 1
                 elif downleft(r,c) in char_map["M"] and upright(r,c) in char_map["S"] and downright(r,c) in char_map["S"]:
                     count += 1
            elif downright(r,c) in char_map["M"]:
                 if upright(r,c) in char_map["M"] and downleft(r,c) in char_map["S"] and upleft(r,c) in char_map["S"]:
                      count += 1
                 elif downleft(r,c) in char_map["M"] and upright(r,c) in char_map["S"] and upleft(r,c) in char_map["S"]:
                      count += 1
            
    print(count)
