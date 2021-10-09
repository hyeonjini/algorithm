import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n = int(input()) # 도시
m = int(input()) # 간선

distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))

a, b = map(int, input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for j in graph[now]:
            # j[0] = node, j[1] = cost
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(a)
print(distance[b])