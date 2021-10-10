"""
파티
"""

import sys
import copy
from heapq import heappop, heappush

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split()) # n: 도시, m: 경로, x: 파티 장소

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라
def dijkstra(start, end, distance):

    distance_copy = copy.deepcopy(distance)

    q = []
    heappush(q, (0, start))
    distance_copy[start] = 0
    while q:
        dist, now = heappop(q)

        if distance_copy[now] < dist:
            continue
        for j in graph[now]:
            cost = j[1] + dist

            if distance_copy[j[0]] > cost:
                distance_copy[j[0]] = cost
                heappush(q, (cost, j[0]))

    return distance_copy[end], distance_copy

to_target = [INF] * (n + 1)

for i in range(1, n + 1):
    to_target[i], _ = dijkstra(i, x, distance)

_, from_target = dijkstra(x, x, distance)

result = 0
for go, back in zip(to_target[1:], from_target[1:]):
    result = max(result, go + back)

print(result)
