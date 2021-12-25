"""
N과 M(8)
"""

import sys

input = sys.stdin.readline

def solution(n, m):
    pass

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    solution(arr, n, m)