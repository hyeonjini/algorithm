"""
안테나
"""
import sys

input = sys.stdin.readline

n = int(input())

home = list(map(int, input().split()))
home.sort()

index = None
if n % 2 == 0:
    index = n // 2 - 1
else:
    index = n // 2
print(home[index])


