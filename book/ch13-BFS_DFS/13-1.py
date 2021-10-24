"""
특정 거리의 도시 찾기
"""
import sys
from heapq import heappop, heappush

INF = int(1e9)

input = sys.stdin.readline

n, m, k, x = map(int, input().split()) # n:도시, m:간선, k:최단거리, x: 시작도시

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 1])

def dijkstra(start):
    q = []
    
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        if dist > distance[now]:
            continue

        for j in graph[now]:
            cost = dist + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heappush(q, (cost, j[0]))

dijkstra(x)
if k not in distance:
    print(-1)

else:
    for i in range(1, n+1):
        if k == distance[i]:
            print(i)
