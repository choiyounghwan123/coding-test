import sys

N = int(sys.stdin.readline())
nums = list(sys.stdin.readline().rstrip())
res = 0
for n in nums:
    res += int(n)
print(res)