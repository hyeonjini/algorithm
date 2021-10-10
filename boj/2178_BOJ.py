import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
    
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상, 하, 좌, 우

q = deque([[0, 0]]) # 시작 지점

while q:
    x, y = q.popleft()
    
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        
        if nx < 0 or ny < 0 or nx > (n-1) or ny > (m-1): # 범위 벗어난것 제외
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append([nx, ny])

print(graph[n-1][m-1])