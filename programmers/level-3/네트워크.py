from collections import deque
import queue

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        
        if visited[i]:
            continue
        
        q = deque([i])
        visited[i] = True
        while q:
            current = q.popleft()

            for j in range(len(computers[current])):
                if computers[current][j] == 0:
                    continue

                if i != j and not visited[j]:
                    visited[j] = True
                    q.append(j)

        answer += 1
        
    return answer


if __name__ == "__main__":
    assert solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1