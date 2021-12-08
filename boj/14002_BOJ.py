"""
가장 긴 증가하는 부분 수열 4 
"""

import sys
input = sys.stdin.readline

def solution(n, arr):
    dp = [[k] for k in arr]
    # print(dp)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                if len(dp[j]) + 1 > len(dp[i]):
                    # print("dp[i]:", dp[i], "dp[j]:", dp[j])
                    dp[i] = dp[j] + [arr[i]]
                    # print("dp[i]:", dp[i], "dp[j]:", dp[j])
    
    # print(dp)
    max_length = 0
    max_arr = []
    for d in dp:
        if len(d) > max_length:
            max_length = len(d)
            max_arr = d
    answer = ' '.join(list(map(str, max_arr)))
    return max_length, answer

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result, answer = solution(n, arr)
    print(result)
    print(answer)