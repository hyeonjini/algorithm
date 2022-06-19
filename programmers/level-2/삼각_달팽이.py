def solution(n):
    answer = []
    matrix = [[0] * n for _ in range(n)]

    x1, y1 = 0, 0
    x2, y2 = n-1, n-1
    num = 1
    temp = 0
    while x1 < n and y1 < n and matrix[x1][y1] == 0:
        # 아래
        for i in range(x1, x2+1):
            matrix[i][y1] = num
            num += 1

        # 오른쪽
        for i in range(y1+1, y2):
            matrix[x2][i] = num
            num += 1

        # 위 
        for i in range(x2, x1, -1):
            matrix[i][y2] = num
            num += 1

        x1, y1 = x1+2, y1+1
        x2, y2 = x2-1, y2-2
        temp += 1
    
    for m in matrix:
        for item in m:
            if item != 0:
                answer.append(item)

    return answer

def print_matrix(matrix):
    for line in matrix:
        print(line)
if __name__ == "__main__":

    assert solution(5) == [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
    assert solution(4) == [1,2,9,3,10,8,4,5,6,7]
    assert solution(6) == [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]