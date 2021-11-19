"""
최종 순위
"""
import sys
from collections import deque

input = sys.stdin.readline

def solution(n, last, changes):
    answer = []
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(i + 1, n):
            graph[last[i]][last[j]] = True
            indegree[last[j]] += 1
    
    # print(graph)
    # print(indegree)

    for change in changes:
        a, b = change
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    
    # cycle check

    # topology
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    

    for i in range(n):
        if len(q) == 0:
            return "IMPOSSIBLE"
        if len(q) >= 2:
            return "?"
        
        now = q.popleft()
        answer.append(str(now))
        for j in range(1, n + 1):
            if graph[now][j] == True:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    return " ".join(answer)
    
if __name__ == "__main__":
    t = int(input())
    answers = []
    for _ in range(t):
        n = int(input())
        last = list(map(int, input().split()))
        change = int(input())
        changes = []
        for _ in range(change):
            changes.append(list(map(int, input().split())))
        answers.append(solution(n, last, changes))

    for answer in answers:
        print(answer)