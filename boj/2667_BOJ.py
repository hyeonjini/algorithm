"""
단지 번호 붙이기
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int , input().rstrip())))

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] # U, D, L, R

group = 0 # 단지
houses = []

for a in range(n):
    for b in range(n):
        if graph[a][b] != 0:
            q = deque([[a, b]])
            graph[a][b] = 0
            group += 1
            house = 1

            while q:
                x, y = q.popleft()

                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or ny < 0 or nx > (n-1) or ny > (n-1):
                        continue

                    if graph[nx][ny] != 0:
                        graph[nx][ny] = 0
                        q.append([nx, ny])
                        house += 1

            houses.append(house)
print(group)
houses.sort()
for house in houses:
    print(house)
