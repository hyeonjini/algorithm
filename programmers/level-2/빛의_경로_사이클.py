"""
빛의 경로 사이클
"""
def solution(grid):
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위, 오른쪽, 아래, 왼쪽

    grid = [list(item) for item in grid]
    start_point = [(i, j) for j in range(len(grid[0])) for i in range(len(grid))]
    
    length = 0
    for line in grid:
        length += len(line)
    
    answer = []

    history = [[0] * length for _ in range(length)]
    print(history)
    for start in start_point:
        for i in range(len(direction)):
        
            x, y = start
            cycle_cost = 0
            d = i
            current_direction = direction[d]

            if history[x][y] != 0:
                continue

            # 탐색
            while True:
                # print(f"current pos {x},{y} ({x * len(grid) + y}) {grid[x][y]}", end=" -> ")
                dest = [x + current_direction[0], y + current_direction[1]]

                if dest[0] < 0:
                    dest[0] = len(grid) -1
                
                if dest[0] >= len(grid):
                    dest[0] = 0
                
                if dest[1] < 0:
                    dest[1] = len(grid[0]) -1
                
                if dest[1] >= len(grid):
                    dest[1] = 0
                
                if history[x*len(grid)+y][dest[0]*len(grid)+dest[1]] == 2:
                    break
                
                else:
                    cycle_cost += 1
                    history[x*len(grid)+y][dest[0]*len(grid)+dest[1]] += 1

                x, y = dest[0], dest[1]
                
                if grid[x][y] == "R":
                    d = (d+1) % 4
                    current_direction = direction[d]

                if grid[x][y] == "L":
                    d = (d-1+4) % 4
                    current_direction = direction[d]
                
                # print(f"move to {x}, {y} {grid[x][y]} ({x*len(grid)+y})")
            answer.append(cycle_cost)

    answer.sort()
    return answer

if __name__ == "__main__":
    grid = ["SL", "LR"]
    # grid = ["S"]
    # grid = ["R", "R"]
    print(solution(grid))