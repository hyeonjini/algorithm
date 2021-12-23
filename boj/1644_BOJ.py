"""
소수의 연속합
"""

import sys
input = sys.stdin.readline

def solution(n):
    answer = 0

    # 소수 만들기
    prime_nums = make_prime_nums(n)

    left = 0
    start = len(prime_nums) - 1

    while left < start:
        total = sum(prime_nums)
        
        if total == n:
            continue    
    return answer

def make_prime_nums(n: int):
    prime_num = []

    a = [False, False] + [True] * (n - 1)
    for i in range(2, n+1):
        if a[i]:
            prime_num.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return prime_num

if __name__ == "__main__":
    n = int(input())

    print(solution(n))
