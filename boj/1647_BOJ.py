"""
도시 분할 계획
"""
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

graph = []

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

graph.sort()

costs = []

for cost, a, b in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        costs.append(cost)

result = sum(costs) - max(costs)
print(result)

