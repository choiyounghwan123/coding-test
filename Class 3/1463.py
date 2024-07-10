# 1로 만들기

import sys

N = int(sys.stdin.readline())

res = 0

while N != 0:
    if N % 3 == 0:
        N = N // 3
        res+=1
    elif 