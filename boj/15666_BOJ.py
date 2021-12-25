"""
N과 M (12)
"""
import sys 
input = sys.stdin.readline

def solution(current, arr, n, m, start):
    if len(current) == m:
        for i in current:
            print(i, end=" ")
        print()
        return

    for j in range(start, n):
        solution(current + [arr[j]], arr, n, m, j)
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    arr.sort()
    for i in range(len(arr)):
        solution([arr[i]], arr, len(arr), m, i)
