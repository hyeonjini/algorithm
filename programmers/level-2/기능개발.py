"""
기능 개발
"""
from collections import deque

def solution(progresses, speeds):
    answer =[]
    p_q = deque(progresses)
    s_q = deque(speeds)
    while p_q:
        print(p_q, answer)
        complete = 0

        for i in range(len(p_q)): # 당일 작업 진행
            p_q[i] += s_q[i]

        while True and p_q:

            if p_q[0] >= 100:
                complete += 1
                p_q.popleft()
                s_q.popleft()
                continue
            
            break

        if complete != 0:
            answer.append(complete)
            
    return answer

if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))