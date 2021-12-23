"""
경사로
"""
import sys
input = sys.stdin.readline

def solution(n, l, paths):
    answer = 0

    # 행 path 검사
    for i in range(n):
        path = paths[i]

        print(path)
        
        if is_path(path):
            answer += 1
        
    # 열 path 검사
    for r in range(n):
        row_path = []
        for j in range(n):
            row_path.append(paths[j][r])

        print(row_path)

        if is_path(row_path):
            answer += 1
        
    return answer

def is_path(path):
    
    return True

if __name__ == "__main__":
    n, l = map(int, input().split())
    paths = []

    for _ in range(n):
        paths.append(list(map(int , input().split())))

    print(solution(n, l, paths))