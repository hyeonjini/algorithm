
# DP를 사용하는 방법 O(N^2)
import bisect

def LIS_DP(arr):
    answer = 0

    dp = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(dp)
    answer = max(dp)
    return answer

# DP와 bisect를 사용하는 방법
def LIS_Bisect(arr):
    dp = [arr[0]]
    for i in range(len(arr)):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            idx = bisect.bisect_left(dp, arr[i])
            dp[idx] = arr[i]
    
    return len(dp)

if __name__ == "__main__":
    arr = [7, 2, 3, 8, 11, 23, 25, 0, 4, 5] # 6

    print(LIS_DP(arr))
    print(LIS_Bisect(arr))