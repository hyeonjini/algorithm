"""
격자상의 경로
"""
import sys
from math import ceil
input = sys.stdin.readline

def solution(n, m, k):
    answer = 0

    if k != 0:
        
        mid_x = ceil(k/m)
        mid_y = k % m if k % m != 0 else m
        mid = [mid_x, mid_y]
        # print("mid", mid)
        end = [(n - mid_x) + 1, (m - mid_y) + 1]
        first_root = find_root(mid)
        second_root = find_root(end)
        answer = first_root * second_root
        # print(first_root, second_root)
    else:
        answer = find_root([n, m])
        # print(answer)

    return answer

def find_root(end):

    end_x, end_y = end
    n = end_x
    m = end_y
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    
    graph[1][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            graph[i][j] = graph[i-1][j] + graph[i][j-1]

    # print(graph)

    return graph[end_x][end_y]

if __name__ == "__main__":

    n, m, k = map(int, input().split())

    print(solution(n, m, k))