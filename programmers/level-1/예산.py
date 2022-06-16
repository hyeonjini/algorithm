def solution(d, budget):
    answer = 0

    d.sort()

    total = 0
    for _d in d:
        if budget - (total + _d) >= 0 :
            total += _d
            answer += 1

    return answer


if __name__ == "__main__":
    d = [1, 3, 2, 5, 4]
    budget = 9
    print(solution(d, budget))