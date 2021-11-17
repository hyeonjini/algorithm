"""
플로이드
"""

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    m = int(input())

    edges = [[10001] * (n + 1) for _ in range(n + 1)]
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                edges[a][b] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        # if edges[a][b] != 10001:
        #     if edges[a][b] > c:
        #         edges[a][b] = c
        # else:
        #     edges[a][b] = c
        if c < edges[a][b]:
            edges[a][b] = c
    # print(edges)
    

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                edges[a][b] = min(edges[a][b], edges[a][k] + edges[k][b])
        
    # print(edges)

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if edges[a][b] == 10001:
                print(0, end = " ")
            else:
                print(edges[a][b], end = " ")
        print()
    

