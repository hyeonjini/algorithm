import sys
input = sys.stdin.readline

n = int(input())
number = [int(input()) for _ in range(n)]
number.sort()

for n in number:
    print(n)