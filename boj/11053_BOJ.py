"""
가장 긴 증가하는 부분수열
"""
import sys
input = sys.stdin.readline

def solution(n, arr):
    dp = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(n, arr))