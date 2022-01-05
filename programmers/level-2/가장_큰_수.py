"""
가장 큰 수
"""
import sys
from functools import cmp_to_key
input = sys.stdin.readline

def solution(numbers):
    answer = ''
    
    cmp_value = cmp_to_key(custom_sort) # custom sort
    numbers.sort(key = cmp_value)

    for number in numbers:
        answer += str(number)

    return str(int(answer))

def custom_sort(x, y):
    if str(x)+str(y) < str(y)+str(x):
        return 1
    elif str(x)+str(y) == str(y)+str(x):
        return 0
    else:
        return -1

if __name__ == "__main__":
    numbers = [0, 0, 0, 0]
    print(solution(numbers))