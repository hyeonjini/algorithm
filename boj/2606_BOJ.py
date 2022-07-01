import sys
from collections import deque

input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input()) # network
    m = int(input()) # edge

    network = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b =list(map(int, input().split()))
        network[a].append(b)
        network[b].append(a)

    visited = [False] * (n + 1)

    visited[1] = True
    q = deque([1])

    while q:
        current = q.popleft()

        for node in network[current]:
            if visited[node] == False:
                visited[node] = True
                q.append(node)

    print(sum([item for item in visited if item]) - 1)
    
