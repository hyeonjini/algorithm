"""
k번째 최단 경로
"""
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = int(1e9)

n, m, k = map(int, input().split()) # n:도시, m:간선

path = [[INF] * k for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    path[start][0] = 0
    while q:
        dist, now = heappop(q)

        for node, cost in graph[now]:
            total_cost = dist + cost
            if total_cost < path[node][k-1]:
                path[node][k-1] = total_cost
                path[node].sort()
                heappush(q, (total_cost, node))

dijkstra(1)
print(path)
for p in path[1:]:
    if p[k-1] == INF:
        print(-1)
    else:
        print(p[k-1])
