
from heapq import heappush, heappop

def solution(jobs):
    
    n = len(jobs)
    answer = 0
    current = 0

    jobs.sort(key=lambda x: x[1])
    
    while jobs:

        for i in range(len(jobs)):
            request_time, process_time = jobs[i]
            if current >= request_time:
                current += process_time
                answer += current - request_time
                jobs.pop(i)
                break

            if i == len(jobs) - 1:
                current += 1
            
    return answer // n


if __name__ == "__main__":
    assert solution([[0, 3], [1, 9], [2, 6]]) == 9