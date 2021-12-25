"""
N과 M (2)
"""
import sys
from itertools import combinations
input = sys.stdin.readline
def solution(n, m):
    arr = [i for i in range(1, (n + 1))]

    combi = list(combinations(arr, m))

    for c in combi:
        if is_asc(c):
            print_answer(c)


def is_asc(arr):
    previous = arr[0]
    for i in range(1, len(arr)):
        if previous > arr[i]:
            return False
        previous = arr[i]
    return True

def print_answer(arr):
    for i in arr:
        print(i, end=' ')
    print()
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    solution(n, m)