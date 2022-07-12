def solution(board):
    
    row = len(board)
    col = len(board[0])

    answer = 0

    for i in range(1, row):
        for j in range(1, col):
            if board[i][j]:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    
    for b in board:
        answer = max(answer, max(b))
            
    return answer ** 2




if __name__ == "__main__":
    assert solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]) == 9
    assert solution([[0,0,1,1],[1,1,1,1]]) == 4