"""
위장
"""
from collections import defaultdict
def solution(clothes):
    answer = 1
    closet = defaultdict(list)

    # key에 따라 dictionary에 종류 추가
    for value, key in clothes:
        closet[key].append(value)
    
    # print(closet)

    # 의상 집합에서 1가지를 뽑는 경우의수 (부위별 선택)
    # 각 부위별 조합은 곱하기로 계산
    # for key in closet.keys():
    #     # print(closet[key])
    #     answer *= combination(len(closet[key]) + 1, 1)

    # 모두 안뽑는 경우도 있을 수 있으니(반드시 한가지 부위는 선택) -1

    # 코드 개선 (1가지를 뽑는 경우의 수 nCr은 n!//1!(n-1)! )
    # 결국 n (종류)

    for key in closet.keys():
        answer *= len(closet[key]) + 1
    return answer - 1

def permutation(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result

def combination(n, r):
    return permutation(n) // (permutation(r) * permutation(n-r))


if __name__ == "__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    # clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    
    print(solution(clothes))
