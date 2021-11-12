"""
인구 이동
"""
import sys
from collections import deque

input = sys.stdin.readline

def movement(x, y, index):

    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n = len(graph)

    union_count = 1

    # 연합국가
    country = 1

    # 연합국가 인구
    population = graph[x][y]

    q = deque()
    q.append((x, y))

    # 연합국가 번호
    united[x][y] = index

    # 연합국가 리스트
    union = []
    union.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1: # 범위를 벗어난 경우
                continue
                        
            sub = abs(graph[x][y] - graph[nx][ny])
            if sub >= l and sub <= r and united[nx][ny] == -1:
                country += 1
                population += graph[nx][ny]
                q.append((nx, ny))
                united[nx][ny] = index
                union.append((nx, ny))

                # 연합 인구 수(연합의 모든 인구수/연합의 모든 나라수)
    union_pop = population // country
    for u_x, u_y in union:
        graph[u_x][u_y] = union_pop

    return union_count

if __name__ == "__main__":
    
    graph = []
    answer = 0
    
    n, l, r = map(int, input().split())
    
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    while True:
        # 연합 번호
        united = [[-1] * n for _ in range(n)]
        index = 0
        for i in range(n):
            for j in range(n):
                if united[i][j] == -1:
                    movement(i, j, index)
                    index += 1
        
        print(graph)

        if index == n * n:
            break
        answer += 1
    print(answer)