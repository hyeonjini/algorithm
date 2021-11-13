import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
fold = []
for _ in range(n):
    heappush(fold, int(input()))

result = 0
while len(fold) != 1:
    first = heappop(fold)
    second = heappop(fold)

    heappush(fold, first + second)
    result += first + second

print(result)