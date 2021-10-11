"""
적록색약
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
visited = [[False] * n for _ in range(n)]
graph= []
graph_blind = []

for _ in range(n):
    line = list(input().rstrip())
    graph.append(line)
    graph_blind.append(line)

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] # U, D, L, R

group_normal = 0
group_blind = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            group_normal += 1

            q = deque([[i, j]])
            visited[i][j] = True

            while q:
                x, y = q.popleft()

                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                        continue
                    if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append([nx, ny])
        
        if graph_blind[i][j] == 'G':
            graph_blind[i][j] = 'R'

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            group_blind += 1

            q = deque([[i, j]])
            visited[i][j] = True

            while q:
                x, y = q.popleft()

                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                        continue
                    if graph_blind[nx][ny] == graph_blind[x][y] and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append([nx, ny])

print(group_normal, group_blind)