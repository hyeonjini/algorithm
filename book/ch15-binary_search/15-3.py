"""
공유기 설치
"""
import sys

input = sys.stdin.readline

def binary_search(arr):

    min_gap = 1
    max_gap = arr[-1] - arr[0]

    result = 0
    
    while min_gap <= max_gap:
        mid = (min_gap + max_gap) // 2
        value = arr[0]
        count = 1

        for i in range(1, n):
            if arr[i] >= value + mid:
                value = arr[i]
                count += 1
        if count >= c:
            min_gap = mid + 1
            result = mid
        else:
            max_gap = mid - 1

    return result

if __name__ == "__main__":
    n, c = map(int, input().split())
    
    x = []
    for _ in range(n):
        x.append(int(input()))
    x.sort()

    print(binary_search(x))
