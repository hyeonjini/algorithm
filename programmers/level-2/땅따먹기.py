def solution(land):
    dp = [[0] * 4 for _ in range(len(land)+1)]
    
    for i in range(1, len(land)+1):
        for j in range(4):
            dp[i][j] = max([dp[i-1][k] for k in range(len(dp[i-1])) if k != j]) + land[i-1][j]

    return max(dp[-1])


if __name__ == "__main__":
    assert solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]) == 16