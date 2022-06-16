def solution(n):

    return sum([item for item in range(1, n+1) if n % item == 0])

n = 12
print(solution(n))