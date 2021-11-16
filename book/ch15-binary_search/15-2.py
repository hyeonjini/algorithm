"""
고정점 찾기
"""
import sys
input = sys.stdin.readline

def solution(arr, n):
    answer = binary_search(arr, 0, n-1)

    if answer == None:
        answer = -1

    return answer

def binary_search(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    target = mid

    if arr[mid] == target:
        return mid
    
    elif arr[mid] < target:
        return binary_search(arr, mid+1, end)
    else:
        return binary_search(arr, start, mid - 1)

if __name__ == "__main__":

    n = int(input())
    arr = list(map(int, input().split()))

    print(solution(arr, n))
