"""
거리두기 확인하기
"""

import sys
from collections import deque
input = sys.stdin.readline

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(places):
    answer = []
    for place in places:

        if bfs(place):
            answer.append(1)
        else:
            answer.append(0)
        # break
    return answer

def bfs(place):

    place = [list(item) for item in place]
    # print(place)  
    for i in range(len(place)):
        for j in range(len(place)):
            if place[i][j] == "P":
                # start bfs
                q = deque([[i, j]])
                visited = [[0] * len(place) for _ in range(len(place))]
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or ny < 0 or nx >= len(place) or ny >= len(place):
                            continue

                        if place[nx][ny] != "X" and visited[nx][ny] == 0:
                            q.append([nx, ny])
                            visited[nx][ny] = visited[x][y] + 1
                            if place[nx][ny] == "P":
                                if visited[nx][ny] != 0 and visited[nx][ny] < 4:
                                    return False
                                
    return True

def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

    print(solution(places))