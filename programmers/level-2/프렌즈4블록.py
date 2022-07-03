def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    while True:
        conduct = pop(m, n, board)
        if conduct == 0:
            break
        answer += conduct
        board = move(m, n, board)

    return answer

def pop(m, n, board) -> int:

    dx = [0, 1, 1]
    dy = [1, 0, 1]

    pop_pos = [[False] * n for _ in range(m)]

    for x in range(m):
        for y in range(n):
            if board[x][y] == "@": # 빈 공간일 경우 넘어감
                continue
            
            condition = True

            for k in range(3):
                nx, ny = x + dx[k], y + dy[k]
                if nx >= m or ny >= n:
                    condition = False
                    continue
                
                if board[nx][ny] != board[x][y]: # 하나라도 다른 경우 k for문 break
                    condition = False
                    break
                
            if condition:
                pop_pos[x][y] = True
                for k in range(3):
                    nx, ny = x + dx[k], y + dy[k]
                    pop_pos[nx][ny] = True
    
    answer = 0
    for x in range(m):
        for y in range(n):
            if pop_pos[x][y]:
                board[x][y] = "@"
                answer += 1

    return answer


def move(m, n, board):
    new_board = [[] for _ in range(m)]

    for col in zip(*board):
        col = list(col)
        new_col = []
        for j in range(m-1, -1, -1):
            if col[j] != "@":
                new_col = [col[j]] + new_col
        
        new_col = ["@"] * (m - len(new_col)) + new_col
        
        for i in range(m):
            new_board[i].append(new_col[i])

    return new_board

def print_matrix(matrix):
    for row in matrix:
        print(row)


if __name__ == "__main__":

    assert solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]) == 14
    assert solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]) == 15 