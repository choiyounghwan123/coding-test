# 덩치

import sys

N = int(sys.stdin.readline())
spec = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
res = []

for i in range(N):
    result = 0
    for j in range(N):
        if i == j:
            continue

        if spec[i][0] < spec[j][0] and spec[i][1] < spec[j][1]:
            result+=1
    res.append(result+1)

for i in res:
    print(i, end=" ")