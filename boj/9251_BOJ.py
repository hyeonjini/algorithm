"""
LCS
Longest Common Subsequence
"""
import sys
input = sys.stdin.readline

def solution(str1, str2):
    answer = 0
    LCS = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

    for i in range(len(str2) + 1):
        for j in range(len(str1) + 1):
            if i == 0 or j == 0: 
                LCS[i][j] = 0

            elif str1[j-1] == str2[i-1]: # 같을 때 왼쪽 위 값 + 1
                LCS[i][j] = LCS[i - 1][j - 1] + 1
            
            else: # 다를 때 유지
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
    
    answer = 0
    for sub in LCS:
        answer = max(answer, max(sub))
    return answer


if __name__ == "__main__":
    str1 = list(input().rstrip())
    str2 = list(input().rstrip())

    print(solution(str1, str2))

