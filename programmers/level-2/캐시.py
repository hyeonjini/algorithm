"""
캐시

LRU Algorithm:
가장 오랫동안 참조되지 않은 페이지를 교체.

"""
from collections import deque
def solution(cacheSize, cities):

    cache = deque(maxlen=cacheSize)
    answer = 0

    for city in cities:

        city = city.lower()

        if city not in cache:
            cache.append(city)
            answer += 5

        else:
            cache.remove(city)
            cache.append(city)
            answer += 1

    return answer

if __name__ == "__main__":

    assert solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 50
    assert solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) == 21
    assert solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 60
    assert solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 52
    assert solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16
    assert solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25