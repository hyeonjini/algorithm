def solution(s):

    s = list(map(int, s.split()))
    answer = ' '.join([str(min(s)), str(max(s))])

    return answer


if __name__ == "__main__":
    assert solution("1 2 3 4") == "1 4"
    assert solution("-1 -2 -3 -4") == "-4 -1"
    assert solution("-1 -1") == "-1 -1"