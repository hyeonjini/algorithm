"""
위장
"""
from collections import defaultdict
from itertools import combinations
def solution(clothes):
    answer = 0
    closet = defaultdict(list)

    for value, key in clothes:
        closet[key].append(value)
    
    # print(closet)

    for key in closet.keys():
        print(closet[key])
        for i in range(len(closet[key]) + 1):
            print(list(combinations(closet[key], i)))
            answer += len(list(combinations(closet[key], i)))
    return answer - 1


if __name__ == "__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    # clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    
    print(solution(clothes))
