"""
프린터
"""
from collections import deque

def solution(priorities, location):
    answer = 0
    work = [[priority, False] for priority in priorities]
    work[location][1] = True
    work = deque(work)
    priorities.sort(reverse=True)

    while work:
        current, target = work.popleft()

        if current >= priorities[0]:
            answer += 1
            priorities = priorities[1:]
            
            if target:
                break
        else:
            work.append([current, target])


    return answer

if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2
    # priorities = [1, 1, 9, 1, 1, 1]
    # location = 0

    print(solution(priorities, location))