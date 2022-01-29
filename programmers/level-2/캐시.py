"""
캐시

LRU Algorithm:
가장 오랫동안 참조되지 않은 페이지를 교체.

"""
from heapq import heappop, heappush, heapify
def solution(cacheSize, cities):
    answer = 0

    
    return answer



if __name__ == "__main__":
    cacheSize = 3
    cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    print(solution(cacheSize, cities))