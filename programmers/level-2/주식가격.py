"""
주식 가격
"""
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        current = prices.popleft()

        for i in range(len(prices)):
            if prices[i] < current:
                answer.append(i+1)
                break
            if i == len(prices)-1:
                answer.append(i+1)
    answer.append(0)
    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))