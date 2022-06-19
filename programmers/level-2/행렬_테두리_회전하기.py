import copy

def solution(rows, columns, queries):
    answer = []
    
    # 행렬 초기화
    matrix = [[j for j in range(i, i+columns)] for i in range(1, rows*columns+1, columns)]

    print_matrix(matrix)
    for query in queries:
        x1, y1, x2, y2 = [x-1 for x in query]

        temp = matrix[x1][y1]
        min_value = temp

        # 위 
        for r in range(x1+1, x2+1):
            matrix[r-1][y1] = matrix[r][y1]
            min_value = min(min_value, matrix[r][y1])

        # 왼쪽
        for c in range(y1+1, y2+1):
            matrix[x2][c-1] = matrix[x2][c]
            min_value = min(min_value, matrix[x2][c])
        # 아래
        for r in range(x2-1, x1-1, -1):
            matrix[r+1][y2] = matrix[r][y2]
            min_value = min(min_value, matrix[r][y2])

        # 오른쪽
        for c in range(y2-1, y1-1, -1):
            matrix[x1][c+1] = matrix[x1][c]
            min_value = min(min_value, matrix[x1][c])
        
        matrix[x1][y1+1] = temp
        answer.append(min_value)
        # break

        print_matrix(matrix)
    return answer

def print_matrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    rows = 6
    columns = 6
    queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

    # rows = 100
    # columns = 97
    # queries = [[1,1,100,97]]

    # rows = 3
    # columns = 3
    # queries = [[1,1,2,2]]
    # assert solution(rows, columns, queries) != 1
    print(solution(rows, columns, queries))