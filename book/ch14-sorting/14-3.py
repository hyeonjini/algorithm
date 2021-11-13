"""
실패율
"""
import sys
input = sys.stdin.readline


def solution(N, stages):
    fail = []

    clear_list = [0] * (N + 2)
    not_clear_list = [0] * (N + 2)

    for stage in stages:
        not_clear_list[stage] += 1
        for j in range(stage, 0, -1):
            clear_list[j] += 1

    for i in range(1, N+1):
        # clear = len(list(filter(lambda x: x >= i, stages)))
        clear = clear_list[i]
        # not_clear = len(list(filter(lambda x: x == i, stages)))
        not_clear = not_clear_list[i]
        if clear == 0:
            rate = 0
        else:
            rate = not_clear / clear
        fail.append((i, rate))
    
    # print(fail)
    fail.sort(key=lambda x : x[1], reverse=True)
    # print(fail)
    answer = [x[0] for x in fail]

    return answer

if __name__ == "__main__":
    N = 5
    stages = [2, 1, 2, 6, 2, 4, 3, 3]

    print(solution(N, stages))