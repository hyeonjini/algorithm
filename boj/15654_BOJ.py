"""
N과 M(5)
"""

import sys
import copy
input = sys.stdin.readline

def solution(arr, removed_arr, m):
    if len(arr) == m:
        for i in arr:
            print(i, end=' ')
        print()
        
    for j in removed_arr:
        temp = copy.deepcopy(removed_arr)
        temp.remove(j)
        solution(arr + [j], temp, m)


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    for i in range(len(arr)):
        temp = copy.deepcopy(arr)
        # solution([i], arr, n, m, visited)
        temp.remove(arr[i])
        solution([arr[i]], temp, m)