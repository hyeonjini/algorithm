import sys
from collections import deque

input = sys.stdin.readline

n, m, start = map(int, input().split())

visited = [False] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for item in graph:
    item.sort()

def dfs(graph, v, visited):

    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):

    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(graph, start, visited)
visited = [False] * (n + 1)
print()
bfs(graph, start, visited)