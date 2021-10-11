"""알파벳"""
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int , input().split())

graph = []

for _ in range(r):
    graph.append(list(input().rstrip()))

direction = [[-1, 0], [1, 0], [0, -1], [0, 1]] # U, D, L, R

alphabet = [False] * 26
alphabet[ord(graph[0][0])-65] = True
max_depth = 1

def dfs(graph, x, y, alphabet, depth):
    global max_depth
    
    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx > (r - 1) or ny > (c - 1):
            continue
        if not alphabet[ord(graph[nx][ny])- 65]:
            alphabet[ord(graph[nx][ny]) - 65] = True
            dfs(graph, nx, ny, alphabet, depth + 1)
            alphabet[ord(graph[nx][ny]) - 65] = False
            
    if max_depth < depth:
        max_depth = depth

dfs(graph, 0, 0, alphabet, 1)

print(max_depth)