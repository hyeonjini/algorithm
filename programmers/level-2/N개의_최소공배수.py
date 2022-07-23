def solution(arr):
    answer = arr[0]

    for i in range(1, len(arr)):
        answer = answer * arr[i] / GCD(answer, arr[i])

    return answer

def GCD(x, y):
    X = max(x, y)
    Y = min(x, y)

    while (X % Y) != 0:
        R = X % Y
        X = Y
        Y = R

    return Y

if __name__ == "__main__":

    assert solution([2, 6, 8, 14]) == 168
    assert solution([1, 2, 3]) == 6