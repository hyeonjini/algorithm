import sys
import heapq

INF = int(1e9)

input = sys.stdin.readline

n, m = map(int , input().split()) # 회사:n, 경로:m

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int , input().split())
    graph[a].append((b, c))
