"""
다리를 지나는 트럭
"""
import sys
from collections import deque
input = sys.stdin.readline

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    running_q = []

    current_weight = 0
   
    while True:

        answer += 1
        for i in range(len(running_q)):
            running_q[i][1] -= 1
            if running_q[i][1] == 0:
                current_weight -= running_q[i][0]
        # print(running_q)

        pop_count = 0
        for i in range(len(running_q)):
            if running_q[i][1] == 0:
                pop_count += 1
        for i in range(pop_count):
            running_q.remove(running_q[0])
        
        if len(truck_weights) > 0 and (truck_weights[0] + current_weight) <= weight and len(running_q) < bridge_length:
            next_truck = truck_weights.popleft()
            current_weight += next_truck
            running_q.append([next_truck, bridge_length])
        
        
        # print(answer, running_q, next_truck, truck_weights, current_weight)
        if not truck_weights and not running_q:
            break
    return answer

if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]

    bridge_length = 100
    weight = 100
    truck_weights = [10]

    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]
    print(solution(bridge_length, weight, truck_weights))