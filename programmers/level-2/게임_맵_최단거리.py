"""
게임 맵 최단거리
"""
from collections import deque
# 상, 하, 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def solution(maps):
    answer = 0

    n, m = len(maps), len(maps[0])
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maps[nx][ny] == 0:
                continue

            if nx == 0 and ny == 0:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                
    # print(maps)
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1

if __name__ == "__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    # maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	
    print(solution(maps))