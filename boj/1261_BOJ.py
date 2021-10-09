import sys
from heapq import heappop, heappush

readline = sys.stdin.readline

n, m = map(int, input().split()) # 열, 행

direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

arr = []
for _ in range(m):
    arr.append(list(map(int, list(input()))))

graph = [[] for _ in range(n * m)]

for i in range(n * m):
    x = i // n
    y = i % n
    for dx, dy in direction: # 상, 하, 좌, 우 연결된 그래프 탐색
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx > m-1 or ny > n-1:
            continue
        
        node = n * nx + ny
        graph[i].append((node, arr[nx][ny]))

# dijskstra
INF = int(1e9)
distance = [INF] * (n * m)

def dijkstra(start):

    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        if dist > distance[now]:
            continue
        
        for j in graph[now]:
            cost = j[1] + dist
            
            if distance[j[0]] > cost:
                distance[j[0]] = cost
                heappush(q, (cost, j[0]))

dijkstra(0)

print(distance[n * m - 1])
