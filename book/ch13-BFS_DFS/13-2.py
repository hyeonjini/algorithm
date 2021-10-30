"""
연구소
"""

import sys
from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline

dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

def do_spread(matrix):
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                q = deque()
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    # 상, 하, 좌, 우 탐색
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if matrix[nx][ny] == 0:
                            matrix[nx][ny] = 2
                            q.append([nx, ny])
    return matrix
                    
def get_safety(matrix):
    count = 0
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                count += 1
    return count

if __name__ == "__main__":

    n, m = map(int, input().split()) # n * m 행렬 입력

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    # 벽 후보 탐색
    wall_location = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                wall_location.append((i, j))
    wall_location = list(combinations(wall_location, 3)) # 전체 벽 위치 후보 중에서 3가지를 뽑는 경우의수
    
    # 벽을 설치 후 바이러스 전파 시작하고 max safety 탐색
    safety = 0
    for p1, p2, p3 in wall_location:
        temp_map = copy.deepcopy(graph)

        # 벽 설치
        temp_map[p1[0]][p1[1]] = 1
        temp_map[p2[0]][p2[1]] = 1
        temp_map[p3[0]][p3[1]] = 1
        # 바이러스 전파
        temp_map = do_spread(temp_map)

        # 안전 구역 계산
        num_safety = get_safety(temp_map)
        safety = max(num_safety, safety)

    print(safety)
    
