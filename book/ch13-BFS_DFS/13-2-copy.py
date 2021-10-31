"""
연구소
1. 3개의 벽을 세우는 모든 경우의 수 모두 탐색 (2중 for)
2. 벽을 세워서 dfs or bfs 로 바이러스 전파 시작
3. 전파된 상태에서 안전한 구역 dfs or bfs로 탐색 시작
"""
import sys
import copy
from pprint import pprint
from itertools import combinations
input = sys.stdin.readline

dx = [0, 0, -1, 1] # 상, 하, 좌, 우
dy = [-1, 1, 0, 0] # 상, 하, 좌, 우

def do_spread(installed_wall):
    pass

def get_safety_area(matrix):
    score = 0

    return score

if __name__ == "__main__":
    
    # input data
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    # get wall locations
    locations = []
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                locations.append((i, j))
    
    # combination
    wall_locations = list(combinations(locations, 3))

    result = 0
    for p1, p2, p3 in wall_locations:
        simulation = copy.deepcopy(graph)
        # set wall
        simulation[p1[0]][p1[1]] = 1
        simulation[p2[0]][p2[1]] = 1
        simulation[p3[0]][p3[1]] = 1

        # do spread virus
        simulation = do_spread(simulation)

        score = get_safety_area(simulation)

        result = max(result, score)
    