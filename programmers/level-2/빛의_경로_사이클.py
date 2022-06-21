"""
빛의 경로 사이클
"""
# def solution(grid):
#     direction = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위, 오른쪽, 아래, 왼쪽

#     grid = [list(item) for item in grid]
#     start_point = [(i, j) for j in range(len(grid[0])) for i in range(len(grid))]
    
#     length = 0
#     for line in grid:
#         length += len(line)
    
#     answer = []

#     cycle = [[0] * length for _ in range(length)]
#     print(cycle)
#     for start in start_point:
#         for i in range(len(direction)):
        
#             x, y = start
#             cycle_cost = 0
#             d = i
#             current_direction = direction[d]

#             if cycle[x][y] != 0:
#                 continue
            
#             # 탐색
#             while True:
#                 # print(f"current pos {x},{y} ({x * len(grid) + y}) {grid[x][y]}", end=" -> ")
#                 dest = [x + current_direction[0], y + current_direction[1]]

#                 if dest[0] < 0:
#                     dest[0] = len(grid) -1
                
#                 if dest[0] >= len(grid):
#                     dest[0] = 0
                
#                 if dest[1] < 0:
#                     dest[1] = len(grid[0]) -1
                
#                 if dest[1] >= len(grid):
#                     dest[1] = 0
                
#                 if cycle[x*len(grid)+y][dest[0]*len(grid)+dest[1]] == 2:
#                     break
                
#                 else:
#                     cycle_cost += 1
#                     cycle[x*len(grid)+y][dest[0]*len(grid)+dest[1]] += 1

#                 x, y = dest[0], dest[1]
                
#                 if grid[x][y] == "R":
#                     d = (d+1) % 4
#                     current_direction = direction[d]

#                 if grid[x][y] == "L":
#                     d = (d-1+4) % 4
#                     current_direction = direction[d]
                
#                 # print(f"move to {x}, {y} {grid[x][y]} ({x*len(grid)+y})")

#             answer.append(cycle_cost)

#     answer.sort()
#     return answer
import sys

sys.setrecursionlimit(10 ** 6)

def out(x, y, d, grid, dic):
    nx = x + dic[d][0]
    ny = y + dic[d][1]
    
    if nx >= len(grid):
        nx = 0
    elif nx < 0:
        nx = len(grid)-1
    
    if ny >= len(grid[0]):
        ny = 0
    elif ny < 0:
        ny = len(grid[0])-1
        
    return nx, ny
    

def dfs(state, org, route, grid):
    dic = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}
    x = state[0]
    y = state[1]
    d = state[2]
    visited[d][x][y] = 1
    
    nx, ny = out(x, y, d, grid, dic)
    value = grid[nx][ny]
    
    if value == 'R':
        d = (d + 5) % 4
        
    elif value == 'L':
        d = (d + 7) % 4
    
    if org[0] == nx and org[1] == ny and org[2] == d:
        answer.append(route)
        return
    
    if not visited[d][nx][ny]:
        dfs([nx, ny, d], org, route+1, grid)
        
def solution(grid):
    global answer, visited
    
    answer = []
    visited = [[[0]*len(grid[0]) for _ in range(len(grid))] for _ in range(4)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                dfs([i, j, d], [i, j, d], 1, grid)
                    
                    
    return sorted(answer)
if __name__ == "__main__":
    grid = ["SL", "LR"]
    grid = ["S"]
    # grid = ["R", "R"]
    print(solution(grid))