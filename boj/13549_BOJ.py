"""
숨바꼭질 3
"""
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def solution(n, k):
    # n 이 더 큰 경우
    # if n >= k:
    #     return n - k

    # k 가 더 큰 경우만 고려
    INF = 100001
    answer = 0
    graph = [-1] * INF
    graph[n] = 0
    q = []
    heappush(q, (0, n))

    while q:
        cost, x = heappop(q)

        for dx in (2*x, x-1, x+1):
            if dx >= 0 and dx < INF and graph[dx] == -1:
                if dx == 2*x:
                    graph[dx] = cost
                    heappush(q, (graph[dx], dx))
                else:
                    graph[dx] = cost + 1
                    heappush(q, (graph[dx], dx))
    # print(graph[:18])
    
    answer = graph[k]
    return answer

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solution(n, k))