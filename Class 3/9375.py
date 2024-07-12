# 패션왕 신해빈

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    hash_map = dict()
    for _ in range(N):
        a,type = map(str,sys.stdin.readline().split())
        hash_map[type] = hash_map.get(type,0) + 1

    res = 0
    prev = 0
    for key,value in hash_map.items():
        res += value
        if prev != 0:
            res += prev * value
        prev = value

    print(res)
