"""
소수의 연속합
"""

import sys
input = sys.stdin.readline

def solution(n):
    answer = 0

    # 소수 만들기
    prime_nums = make_prime_nums(n)
    # print(prime_nums)
    left = 0
    right = 0

    while right < len(prime_nums):
        total = sum(prime_nums[left:right+1])
        # print("total:", prime_nums[left:right+1])
        if total == n:
            answer += 1
            right += 1
            # print("find")

        if total < n:
            right += 1
        else:
            left += 1
          
    return answer

def make_prime_nums(n: int):
    prime_num = []

    a = [False, False] + [True] * (n - 1)
    # print(a)
    for i in range(2, n+1):
        if a[i]:
            prime_num.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False

    return prime_num

if __name__ == "__main__":
    n = int(input())

    print(solution(n))
