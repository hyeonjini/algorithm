"""
금광
"""
import sys
input = sys.stdin.readline

def solution():
    
    r, c = map(int, input().split())

    data = list(map(int, input().split()))
    arr = []

    for i in range(0, len(data), c):
        arr.append(data[i:i+c])

    print(arr)

    # dp table
    dp = [[0]* c for _ in range(r)]
    pre_pos = [(1, -1), (0, -1), (-1, -1)] # 왼쪽 아래, 왼쪽, 왼쪽 위

    for k in range(r):
        dp[k][0] = arr[k][0] # dp table 초기화
        
    for j in range(1, c):
        for i in range(r):
            max_value = 0
            for dx, dy in pre_pos:
                nx = dx + i
                ny = dy + j
                if nx < 0 or nx >= r:
                    continue
                max_value = max(max_value, dp[nx][ny])
            dp[i][j] = arr[i][j] + max_value
    
    return max([row[-1] for row in dp])
    
if __name__ =="__main__":
    case = int(input())

    answers = []
    for _ in range(case):
        answers.append(solution())
    
    for ans in answers:
        print(ans)
