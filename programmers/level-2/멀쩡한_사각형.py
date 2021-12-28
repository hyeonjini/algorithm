"""
멀쩡한 사각형
"""

import sys
input = sys.stdin.readline

def solution(w,h):
    answer = w * h
    pattern = gcd(w, h)
    print("pattern:", pattern)
    w, h = w // pattern, h // pattern
    
    print("w, h", w, h)
    if w == 1 or h == 1:
        unusable = w * h
    else:
        unusable = w + h - 1

    print("unusable:", unusable)
    return answer - pattern * unusable

def gcd(w, h):
    while h:
        w, h = h, w % h
    
    return w

if __name__ == "__main__":
    w = 2
    h = 5

    print(solution(w, h))
