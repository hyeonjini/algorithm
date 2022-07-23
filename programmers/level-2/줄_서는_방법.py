from itertools import permutations

def solution(n, k):

    answer = []
    
    rest = [i for i in range(1, n + 1)]

    print(rest)

    while len(rest) > 1:

        n = factorial(len(rest) - 1)
        group = (k-1) // n
        answer.append(rest.pop(group))
        k = k % n 

    answer += rest

    return answer

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# def factorial(n):
#     if n == 1:
#         return n
#     return n * factorial(n-1)

if __name__ == "__main__":
    assert solution(3, 5) == [3, 1, 2]
    assert solution(4, 9) == [2, 3, 1, 4]