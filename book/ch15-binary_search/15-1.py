"""
정렬된 배열에서 특정 수의 개수 구하기
"""
import sys

input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

count = 0

def first(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == 0 or arr[mid-1] < target) and arr[mid] == target:
        return mid

    elif arr[mid] >= target:
        return first(arr, target, start, mid-1)
        
    else:
        return first(arr, target, mid+1, end)

def last(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == n-1 or arr[mid + 1]> target) and arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return last(arr, target, start, mid-1)

    else:
        return last(arr, target, mid+1, end)

a = first(arr, x, 0, n-1)
b= last(arr, x, 0, n-1)
if a == None:
    a = 0
print(b-a+1)