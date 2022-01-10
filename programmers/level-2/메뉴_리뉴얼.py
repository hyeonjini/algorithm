"""
메뉴 리뉴얼
"""
from itertools import combinations
def solution(orders, course):
    answer = []

    for c in course:
        count = {}
        for order in orders:
            comb = list(combinations(list(order), c))
            for i in range(len(comb)):
                set_menu = ''.join(sorted(comb[i]))
                if set_menu not in count.keys():
                    count[set_menu] = 1
                else:
                    count[set_menu] += 1
        
        if len(count) == 0:
            continue
        max_value = max(count.values())
        if max_value < 2:
            continue
        for keys in count.keys():
            if count[keys] == max_value:
                answer.append(keys)
    answer.sort()
    return answer

if __name__ == "__main__":
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    # orders = ["XYZ", "XWY", "WXA"]
    course = [2,3,4]

    print(solution(orders, course))