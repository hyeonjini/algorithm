"""
N과 M (4)
"""
import sys
from itertools import product
input = sys.stdin.readline

def solution(n, m):
    answer = 0
    arr = [i for i in range(1, (n + 1))]

    for start in arr:
        dfs([start], n, m, start)
    
    return answer

def dfs(arr, n, m, start):
    if len(arr) == m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(start, (n+1)):
        dfs(arr + [i], n, m, i)


if __name__ == "__main__":
    n, m = map(int, input().split())
    solution(n, m)
    