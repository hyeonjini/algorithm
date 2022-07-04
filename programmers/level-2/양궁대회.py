# not yet
from collections import deque
def solution(n, info):
    answer = []
    # for i in range(11): # 과녁의 점수는 10 ~ 0까지

    ryan = [[n, [0] * (len(info))]]
    for i in range(len(info)):
        for r in ryan:
            res, score = r
            print(res, score)
    return answer

if __name__ == "__main__":
    assert solution(5, [2,1,1,1,0,0,0,0,0,0,0]) == [0,2,2,0,1,0,0,0,0,0,0]
    # assert solution(1, [1,0,0,0,0,0,0,0,0,0,0]) == [-1]
    assert solution(9, [0,0,1,2,0,1,1,1,1,1,1]) == [1,1,2,0,1,2,2,0,0,0,0]
    assert solution(10, [0,0,0,0,0,0,0,0,3,4,3]) == [1,1,1,1,1,1,1,1,0,0,2]