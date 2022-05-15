
def solution(n, left, right):

    metrix = [[0] * n for i in range(n)]

    
    for i in range(n):
        metrix[i][i] = i

    print(metrix)

    return None

if __name__ == "__main__":
    n = 3
    left = 2
    right = 5

    print(solution(n, left, right))
