"""
1 2 3 더하기
각 조합 경우의 수 합으로 나타낼 수 있음
"""
import sys
input = sys.stdin.readline

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

n = int(input())

T = []
for _ in range(n):
    T.append(str(dp[int(input())]))

print("\n".join(T))