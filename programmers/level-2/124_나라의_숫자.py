"""
124 나라의 숫자
"""

import sys
input = sys.stdin.readline

def solution(n):
    answer = ''
    parser = [4, 1, 2]

    while n > 0:
        
        answer = str(parser[n%3]) + answer
        if n % 3 == 0:
            n -= 1

        n //= 3
        
    return answer

if __name__ == "__main__":
    n = int(input())
    print(solution(n))