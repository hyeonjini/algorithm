def solution(n):
    if n <= 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for k in range(2, n+1):
        dp[k] = (dp[k-1] + dp[k-2])% 1000000007
    
    return dp[n]

if __name__ =="__main__":
    assert solution(4) == 5, print(solution(4))

    print(solution(0))