"""
11441 합 구하기
"""
import sys
input = sys.stdin.readline

def solution(arr, m):
    answer = 0

    prefix_sum = [0] * (len(arr) + 1)

    for i in range(1, len(arr) + 1):
        prefix_sum[i] = prefix_sum[i-1]+arr[i-1]
    
    for i, j in m:
        print(prefix_sum[j] - prefix_sum[i-1])
    return answer

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    m = []
    for _ in range(int(input())):
        m.append(list(map(int, input().split())))
    
    solution(arr, m)