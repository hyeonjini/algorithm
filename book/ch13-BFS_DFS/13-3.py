"""
경쟁적 전염
"""
import sys
import copy

input = sys.stdin.readline

dx = [-1, 1, 0, 0] # 상, 하, 좌, 우    
dy = [0, 0, -1, 1]

def do_spread(matrix, visited):
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0 and visited[i][j] == False:
                x, y = i, j
                visited[i][j] = True

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        continue
                    
                    if matrix[nx][ny] == 0 and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        matrix[nx][ny] = matrix[i][j]
            
if __name__ == "__main__":
    n, m = map(int, input().split())
    examiner = []
    for _ in range(n):
        line = list(map(int, input().split()))
        examiner.append(line)
    
    s, x, y = map(int, input().split())

    visited = [[False] * m for _ in range(n)]
    for sec in range(0, s):
        do_spread(examiner, copy.deepcopy(visited))
    print(examiner[x-1][y-1])