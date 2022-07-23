def solution(n):
    answer = [1] * (n + 1)

    for i in range(2, n + 1):
        answer[i] = answer[i-2] + answer[i - 1]
    print(answer)
    return answer[n] % 1234567


if __name__ == "__main__":

    assert solution(4) == 5
    assert solution(3) == 3

