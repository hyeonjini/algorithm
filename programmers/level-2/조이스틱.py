def solution(name):
    answer = 0

    while True:
        answer += minimum_distance(26, ord(name[current]) - 26, ord("A"))
        name[current] = "A"
        candidate = [idx for idx, d in enumerate(get_diff(name)) if d != 0]
        if len(candidate) == 0:
            break

        # 가장 가까운 변경점 찾기
        distance = 10000
        idx = len(name) + 1
        for c in candidate:
            d = minimum_distance(len(name), current, c)
            if d < distance:
                distance = d
                idx = c
        current = idx
        answer += distance

    return answer

def get_diff(name):
    return [ord(n) - ord(a) for n, a in zip(name, "A"*len(name))]

def minimum_distance(length, current:int, target:int) -> int:
    if target > current:
        return min((target - current), (current + length - target))

    elif current > target:
        return min((current - target), (target + length - current))

    else:
        return 0

def solution(name):
    answer = 0
    length = len(name)
    move = len(name) - 1

    for i in range(length):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)

        next = i + 1
        while next < length and name[next] == 'A':
            next += 1
        move = min(move, i * 2 + length - next)
        move = min(move, (length - next) * 2 + i)

    return answer + move

if __name__ == "__main__":

    assert solution("JERONE") == 56
    assert solution("JAZ") == 11
    assert solution("ZAZ") == 3
    assert solution("AAAA") == 0
    assert solution("AAAAAZ") == 2, solution("AAAAAZ")
    assert solution("A") == 0
    assert solution("Z") == 1
    assert solution("M") == 12, solution("M")
    assert solution("AZZA") == 4
    assert solution("AAAZZA") == 5
    assert solution("BBBAAAAB") == 8, solution("BBBAAAAB")
    assert solution("ABABAABA") == 9
    assert solution("AAAABABAAAA") == 8
    assert solution("JAAAAAAAN") == 23
    assert solution("ZZZ") == 5 
    assert solution("JAJAAAJ") == 31, solution("JAJAAAJ")
    print(solution("BBBAABB"))