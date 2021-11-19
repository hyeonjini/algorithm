"""
행성 터널
"""
import sys
input = sys.stdin.readline


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
    
if __name__=="__main__":
    n = int(input())
    # parent table 초기화
    parent = [0] * n
    for i in range(n):
        parent[i] = i

    x, y, z = [], [], []
    for i in range(n):
        data = list(map(int, input().split()))
        x.append((data[0], i))
        y.append((data[1], i))
        z.append((data[2], i))
    x.sort()
    y.sort()
    z.sort()

    # data = []
    # for i in range(n):
    #     data.append(list(map(int, input().split())))
        
    # edges = []
    # for i in range(n):
    #     xi, yi, zi = data[i]
    #     for j in range(n):
    #         if i != j:
    #             xj, yj, zj = data[j]
    #             cost = min(abs(xi - xj), abs(yi - yj), abs(zi - zj))
    #             edges.append((cost, i, j))
    edges = []
    for i in range(n - 1):
        cost = x[i + 1][0] - x[i][0]
        a, b = x[i][1], x[i + 1][1]
        edges.append((cost, a, b))

        cost = y[i + 1][0] - y[i][0]
        a, b = y[i][1], y[i + 1][1]
        edges.append((cost, a, b))

        cost = z[i + 1][0] - z[i][0]
        a, b = z[i][1], z[i + 1][1]
        edges.append((cost, a, b))

    edges.sort()
    # print(edges)
    
    
    result = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            result += cost
            union_parent(parent, a, b)
    print(result)