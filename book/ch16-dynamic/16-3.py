"""
퇴사
"""
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    schedule = []
    T = []
    P = []
    for _ in range(n):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)

    dp = [0] * (n+1)
    max_value = 0

    for i in range(n-1, -1, -1):
        
        if T[i] + i <= n:
            dp[i] = max(P[i]+ dp[T[i] + i], max_value)
            max_value = dp[i]
        else:
            dp[i] = max_value

# print(dp)
print(max_value)