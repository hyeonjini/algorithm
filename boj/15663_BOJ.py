"""
N과 M (9)
"""

import sys
from itertools import permutations
input = sys.stdin.readline

def solution(arr, m):

    combi = list(set(permutations(arr, m)))

    combi.sort()
    for c in combi:
        for i in c:
            print(i, end=" ")
        print()
    


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # arr = list(set(arr))
    arr.sort()
    solution(arr, m)