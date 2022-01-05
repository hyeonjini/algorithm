"""
뉴스 클러스터링
"""
import sys
import re
from itertools import combinations
input = sys.stdin.readline


def solution(str1, str2):
    answer = 0
    str1 = preprocessing(str1)
    str2 = preprocessing(str2)
    # 전처리 (2개씩 끊어서 원소 만들기 + 알파벳아닌문자 포함 원소 제거 + 대문자로 변환)
    print(str1, str2)

    # 중복 교집합, 합집합
    inter = duplicate_inter_set(str1, str2)
    differ = duplicate_differ_set(str1, str2)

    if (len(inter) == 0) and (len(differ) == 0): # 공집합
        return 1
    
    answer = len(inter) / len(differ)

    print(answer)
    return int(answer * 65536)

def preprocessing(str):
    items = [str[i:i+2] for i in range(len(str) - 1)]
    return [item.upper() for item in items if item.isalpha()]

def duplicate_inter_set(set1, set2):

    set1 = set1.copy()
    set2 = set2.copy()

    inter = []

    for a in set1:
        if a in set2:
            inter.append(a)
            set2.remove(a)

    return inter

def duplicate_differ_set(set1, set2):

    set1 = set1.copy()
    set2 = set2.copy()

    differ = []
    temp = []

    for a in set1:
        if a not in set2:
            differ.append(a)
        else:
            set2.remove(a)
            temp.append(a)

    return differ + set2 + temp

if __name__ == "__main__":
    str1 = ""
    str2 = ""
    
    print(solution(str1, str2))