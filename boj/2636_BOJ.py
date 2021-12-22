"""
    치즈
"""
import sys
import time
from collections import deque
from pprint import pprint
input = sys.stdin.readline

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]


def solution(h, w, graph):
    hour = 0
    pre_cheese = get_cheese(graph, w, h)
    while True:
        # print("="*20)
        # pprint(graph)
        visited = [[False] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                outter = False
                if graph[i][j] == 0 and visited[i][j] == False:  # 공간을 만나면
                    outter = is_outter(graph, visited, i, j, w, h)
                    
                if outter == True:
                    graph = get_boundary(graph, i, j, w, h)
        # pprint(graph)
        graph = after_an_hour(graph, w, h)
        # pprint(graph)
        cheese = get_cheese(graph, w, h)
        # print("Cheese:", get_cheese(graph, w, h))
        hour += 1
        if cheese == 0:
            break

        pre_cheese = cheese
        
        
    print(hour)
    print(pre_cheese)

def get_cheese(graph, w, h):
    cheese = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                cheese += 1
    return cheese

def is_outter(graph, visited, x, y, w, h):
    outter = False
    q = deque([])
    q.append([x, y])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx >= h or ny >= w or nx < 0 or ny < 0: # 벽을 만나면 outter
                return True
            
            if visited[nx][ny] == False and graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append([nx, ny])
    
    return outter


def get_boundary(graph, x, y, w, h):

    visited = [[False] * w for _ in range(h)]

    q = deque([])
    q.append([x, y])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx >= h or ny >= w or nx < 0 or ny < 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 7
                visited[nx][ny] = True

            if visited[nx][ny] == False and graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append([nx, ny])

    return graph

def after_an_hour(graph, w, h):
    "없어질 치즈 제거하기"
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 7:
                graph[i][j] = 0
    return graph
if __name__ == "__main__":
    h, w = map(int, input().split())

    graph = []
    for _ in range(h):
        line = list(map(int, input().split()))
        graph.append(line)
    # start = time.time()
    
    solution(h, w, graph)
    # print("time: ", time.time() - start)