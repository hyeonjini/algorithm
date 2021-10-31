"""
괄호 변환
"""
import sys
input = sys.stdin.readline


def solution(p):

    left = []
    right = []
    for i in range(len(p)):
        if p[i] == "(":
            left.append("(")
        else:
            right.append(")")
    

if __name__ == "__main__":

    p = list(input().rstrip())
    print(p)