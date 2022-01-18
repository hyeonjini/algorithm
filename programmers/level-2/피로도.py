"""
피로도
"""
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    permut_dungeons = list(permutations(dungeons))

    for permut in permut_dungeons:
        answer = max(answer, get_cost(k, permut))

    return answer

def get_cost(k, dungeons):
    result = 0

    for need, cost in dungeons:
        if k >= need:
            k -= cost
            result += 1
        else:
            break
    
    return result

if __name__ == "__main__":
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]

    # k = 40
    # dungeons = [[50, 10], [40, 10]]

    # k = 5
    # dungeons = [[3, 1], [2, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]



    print(solution(k, dungeons))