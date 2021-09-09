import sys
input = sys.stdin.readline

n = int(input())

coor = []

for _ in range(n):
    coor.append(list(map(int, input().split())))

coor.sort(key=lambda x: (x[0], x[1]))

for c in coor:
    print(c[0], c[1])