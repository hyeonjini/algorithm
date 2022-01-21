"""
전력망을 둘로 나누기
"""
from collections import deque
from copy import deepcopy
def solution(n, wires):
    answer = int(1e9)

    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires: # a, b 둘을 나눔
        # get_node_count(a, b, deepcopy(graph))
        answer = min(answer, get_node_count(a, b, graph))
    return answer

def get_node_count(a, b, graph):
    graph[a].remove(b)
    graph[b].remove(a)
    group_a = bfs(a, graph)
    group_b = bfs(b, graph)
    graph[a].append(b)
    graph[b].append(a)
    return abs(group_a - group_b)

def bfs(start, graph):
    node_count = 1

    visited = [False] * 101
    visited[start] = True
    q = deque([start])

    while q:
        current = q.popleft()
        for i in graph[current]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
                node_count += 1

    return node_count

if __name__ == "__main__":
    n = 9
    wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
    print(solution(n, wires))