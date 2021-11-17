"""
병사 배치하기
LIS 알고리즘 (N^2)
"""

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    
    n = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(n - max(dp))
