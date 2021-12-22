"""
두 로봇
"""
import sys
from collections import deque

input = sys.stdin.readline


def solution(n, r1, r2, graph):
    answer = bfs_path(n, graph, r1, r2)
    # answer = sum(costs) - max(costs)

    return answer


def bfs_path(n, graph, start, target):
    q = deque([(start, 0, 0)])
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        now, total, max_cost = q.popleft()
        if now == target:
            return total - max_cost
        now = graph[now]
        for i, cost in now:
            if visited[i]:
                continue
            else:
                visited[i] = True
                q.append((i, total + cost, max(max_cost, cost)))

    # while q:
    #     now, costs = q.popleft()
    #     if now == target:
    #         return costs
    #     now = graph[now]
    #     for i in range(1, n + 1):
    #         if visited[i] == True or now[i] == 0:
    #             continue
    #         else:
    #             visited[i] = True
    #             q.append((i, costs + [now[i]]))

    return None


def dfs_paths(graph, start, target):
    stack = [(start, [])]
    visited = [False] * (n + 1)
    visited[start] = True

    while stack:
        now, costs = stack.pop()
        # print(path)
        if now == target:
            # print(costs)
            return costs

        now = graph[now]
        for i, cost in now:
            if visited[i]:
                continue
            else:
                visited[i] = True
                stack.append((i, costs + [cost]))

    return None


if __name__ == "__main__":
    n, r1, r2 = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    # graph = [[0] * (n+1) for _ in range(n+1)]
    # # print(graph)
    # for _ in range(n - 1):
    #     a, b, c = map(int, input().split())
    #     graph[a][b] = c
    #     graph[b][a] = c

    print(solution(n, r1, r2, graph))
