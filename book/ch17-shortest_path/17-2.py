"""
정확한 순위
"""
import sys
import copy
from heapq import heappop, heappush

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, graph, distance):
    q = []

    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
    
    return distance


if __name__ == "__main__":
    n, m = map(int, input().split())
    
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append([b, 1])
    
    for i in range(1, n + 1):
        result = dijkstra(i, graph, copy.deepcopy(distance))
        print(result)