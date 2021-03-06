"""
1로 만들기
1. X가 3으로 나누어 떨어지면 3으로 나눈다.
2. 2로 나누어 떨어지면 2로 나눈다.
3. 1을 뺀다.
"""

import sys
input = sys.stdin.readline

INF = int(1e6)

n = int(input())

dp = [INF] * (n + 1)
dp[1] = 0

for i in range(2, n + 1):
    # 1을 뺀 경우
    dp[i] = dp[i - 1] + 1

    # 2로 나눈 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 3으로 나눈경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])

