"""
감시 피하기
"""
import sys
import copy
from itertools import combinations

input = sys.stdin.readline

def find_student(graph):
    
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'T':
                nx, ny = i, j
                # 왼쪽
                while ny > 0:
                    ny -= 1
                    if graph[nx][ny] == 'O':
                        break
                    if graph[nx][ny] == 'S':
                        return False
                ny = j
                # 오른쪽
                while ny < len(graph[i])-1:
                    ny += 1
                    if graph[nx][ny] == 'O':
                        break
                    if graph[nx][ny] == 'S':
                        return False
                ny = j
                # 위
                while nx > 0:
                    nx -= 1
                    if graph[nx][ny] == 'O':
                        break
                    if graph[nx][ny] == 'S':
                        return False
                nx = i
                # 아래
                while nx < len(graph)-1:
                    nx += 1
                    if graph[nx][ny] == 'O':
                        break
                    if graph[nx][ny] == 'S':
                        return False
            else:
                continue
    
    return True
    

def install_obstacle(graph, locs):

    for loc in locs:
        x, y = loc
        graph[x][y] = 'O'

    return graph

if __name__ == "__main__":
    
    n = int(input()) # NxN 입력
    answer = "NO"
    graph = []
    empty = []

    for x in range(n):
        data = input().split()
        graph.append(data)
        for y, k in enumerate(data):
            if k == 'X':
                empty.append((x, y))
    
    obstacle_locs = list(combinations(empty, 3))

    for locs in obstacle_locs:
        
        temp_graph = install_obstacle(copy.deepcopy(graph), locs)

        if find_student(temp_graph):
            answer = "YES"
            break

    print(answer)