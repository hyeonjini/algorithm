"""
더 맵게
"""
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            heapq.heappush(scoville, first)
            break
        
        try:
            second = heapq.heappop(scoville)
        
        except:
            answer = -1
            break

        heapq.heappush(scoville, first + second * 2)
        answer += 1

    return answer

if __name__ == "__main__":
    scoville = [1, 6]
    k = 7

    print(solution(scoville, k))