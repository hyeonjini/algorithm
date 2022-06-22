from collections import deque

def solution(tickets):
    answer = []

    port = []
    for ticket in tickets:
        port.append(ticket[0])
        port.append(ticket[1])
    port = sorted(list(set(port)))
    graph = [[0] * len(port) for _ in range(len(port))]
    
    for ticket in tickets:
        graph[port.index(ticket[0])][port.index(ticket[1])] = 1

    route = [port.index("ICN")]

    while route:
        current = route.pop()
        answer.append(port[current])
        for j in range(len(graph[current])):
            if graph[current][j] == 1:
                route.append(j)
                graph[current][j] =0
                break
        

    return answer

assert solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"]
assert solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]