"""
팰린드롬
문자열 s가 주어질 때, S의 부분 문자열 중 가장 긴 팰린드롬의 길이를 return하는 solution 함수를 완성
"""
import copy
def solution(s):
    answer = 0

    for i in range(len(s) + 1, 0, -1):
        substrings = get_substring(copy.deepcopy(s), i)
        # print(substrings)
        for substring in substrings:
            if is_palindrome(substring):
                # print(substring)
                answer = len(substring)
                return answer
        
    return answer

def is_palindrome(s):
    for i in range(len(s)//2):
        sym = len(s) - i - 1
        if s[i] != s[sym]:
            return False
    return True

def get_substring(s, length):
    substrings = []
    for i in range(len(s)-length + 1):
        substrings.append(s[i:i+length])
    return substrings

if __name__ == "__main__":

    s = "abacde"
    print(solution(s))