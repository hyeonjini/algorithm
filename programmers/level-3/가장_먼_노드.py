
import heapq
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append([1, b])
        graph[b].append([1, a])

    INF = 1e9
    distance = [INF] * (n + 1)

    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        dist, current = heapq.heappop(q)

        if distance[current] < dist:
            continue

        for c, n in graph[current]:
            cost = dist + c
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))


    max_value = max(distance[1:])
    
    answer = len([item for item in distance if item == max_value])
    
    return answer


if __name__ == "__main__":
    assert solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]) == 3