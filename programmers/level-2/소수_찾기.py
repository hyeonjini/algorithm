"""
소수 찾기
"""
import math
from itertools import permutations

def solution(numbers):
    answer = 0
    prime_numbers = []
    numbers = list(numbers)
    for i in range(1, len(numbers) + 1):
        permutation = list(permutations(numbers, i))
        for p in permutation:
            number = int(''.join(p))
            if is_prime_number(number) and number not in prime_numbers:
                answer += 1
                prime_numbers.append(number)
    # prime_numbers.remove(1)
    # print(prime_numbers)
    return answer

def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

if __name__ == "__main__":
    numbers = "17"
    print(solution(numbers))