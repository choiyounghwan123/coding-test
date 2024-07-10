# 랜선 자르기

import sys

K,N = map(int,sys.stdin.readline().split())
res = 0
lines = [int(sys.stdin.readline()) for _ in range(K)]

for i in range(1,max(lines)+1):
    num = 0
    for line in lines:
        num += line // i

    if num >= N:
        res = i
print(res)
