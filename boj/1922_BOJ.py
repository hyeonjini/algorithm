import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else:
        parent[a] = b

if __name__ == "__main__":
    n = int(input())
    e = int(input())

    edges = []
    for _ in range(e):
        a, b, c = list(map(int, input().split()))
        edges.append([a, b, c])

    parent = []
    for i in range(n + 1):
        parent.append(i)

    answer = 0 
    edges = sorted(edges, key=lambda x:x[2])

    for e in edges:
        a, b, c = e
        if find_parent(parent, a) != find_parent(parent, b):
            answer += c
            union_parent(parent, a, b)

    print(answer)
        