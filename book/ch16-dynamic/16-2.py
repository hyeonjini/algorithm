"""
정수 삼각형
"""
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    # print(arr)

    dp = [[0] * i for i in range(1, n + 1)]
    dp[0] = arr[0]
    # print(dp)

    for i in range(1, n):
        for j in range(i + 1):
            if j - 1 < 0:
                dp[i][j] = arr[i][j] + dp[i-1][j]
            elif i - 1 < j:
                dp[i][j] = arr[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]
    # print(dp)

    print(max(dp[-1]))