"""
메뉴 리뉴얼
"""
from pprint import pprint
def solution(orders, course):
    answer = []
    matrix = [[0] * 35 for _ in range(35)]

    for order in orders:
        order = list(order)
        for i in order:
            for j in order:
                if i != j:
                    matrix[ord(i) - 65][ord(j) - 65] += 1
    pprint(matrix)
    return answer

if __name__ == "__main__":
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]

    print(solution(orders, course))