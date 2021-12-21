"""
센서
"""

import sys

input = sys.stdin.readline

def solution(n, k, sensor):
    answer = 0
    sensor.sort()
    distance = []
    for i in range(n-1):
        distance.append(sensor[i+1] - sensor[i])
    
    distance.sort(reverse=True)
    answer = sum(distance[k-1:])
    return answer

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    sensor = list(map(int, input().split()))
    print(solution(n, k, sensor))