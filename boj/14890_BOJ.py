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
        
        if is_path(path, l):
            answer += 1
        
    # 열 path 검사
    for r in range(n):
        row_path = []
        for j in range(n):
            row_path.append(paths[j][r])

        print(row_path)

        if is_path(row_path, l):
            answer += 1
        
    return answer

def is_path(path, l):
    
    up_boundary = []
    down_boundary = []
    previous = path[0]
    for i in range(1, len(path)):
        if previous < path[i]:
            if path[i] - previous > 1:
                return False
            up_boundary.append(i) # 언덕이 시작되는 부분

        elif previous > path[i]:
            if previous - path[i] > 1:
                return False
            down_boundary.append(i - 1) # 언덕이 끝나는 부분
        
        previous = path[i]

    print(up_boundary)
    print(down_boundary)
    return True

if __name__ == "__main__":
    n, l = map(int, input().split())
    paths = []

    for _ in range(n):
        paths.append(list(map(int , input().split())))

    print(solution(n, l, paths))

    # tokenizer test
    is_path([2, 1, 1, 1, 1, 2, 2, 3], 2)
