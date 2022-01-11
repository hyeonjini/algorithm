"""
배달
"""
import sys
from heapq import heappop, heappush
INF = int(1e9)
def solution(N, road, K):
    answer = 0
    distance = [INF] * (N + 1)
    graph = [[] for _ in range(N+1)]

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    answer = len([x for x in dijkstra(graph, 1, distance.copy()) if x <= K])

    return answer

def dijkstra(graph, start, distance):
    q = []
    distance[start] = 0
    heappush(q, (0, start))

    while q:
        dist, current = heappop(q)

        if dist > distance[current]:
            continue

        for i in graph[current]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

    return distance


if __name__ == "__main__":
    N = 5
    road = 	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    K = 3

    print(solution(N, road, K))