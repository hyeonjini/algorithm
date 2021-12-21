"""
    ABCDE
"""

import sys

input = sys.stdin.readline


answer = 0

def solution(n, m, relation):
    global answer

    graph = [[] for _ in range(2000)]
    for a, b in relation:
        graph[a].append(b)
        graph[b].append(a)

    for i in range(2000):
        
        visited = [False] * (2000)
        visited[i] = True
        # print("line : ", i)
        dfs(visited, graph, graph[i], 0)
    
    return answer

def dfs(visited, graph, current, depth):
    
    global answer

    # print("depth:", depth)
    if depth >= 4:
        answer = 1
        return

    for k in current:
        if visited[k] == False:
            visited[k] = True
            dfs(visited, graph, graph[k], depth + 1)
            visited[k] = False

if __name__ == "__main__":
    n, m = map(int, input().split())
    relation = []
    
    for _ in range(m):
        a, b = map(int, input().split())
        relation.append([a, b])
    # print("max :", max_value)
    print(solution(n, m, relation))