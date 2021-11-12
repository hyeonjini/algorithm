"""
감시 피하기
"""
import sys
from itertools import combinations

input = sys.stdin.readline

def find_student(graph):
    pass

def install_obstacle(graph, obstacle_loc):
    pass

if __name__ == "__main__":
    
    n = int(input()) # NxN 입력

    graph = []
    empty = []

    for x in range(n):
        data = input().split()
        graph.append(data)
        for y, k in enumerate(data):
            if k == 'X':
                empty.append((x, y))
    
    obstacle_loc = list(combinations(empty, 3))