from collections import deque
import time

# direction = [(0, 1), (1, 0), (1, 1)] # 오른쪽, 아래, 오른쪽 아래

# def solution(n, left, right):

#     metrix = [[0] * n for i in range(n)]
#     metrix[0][0] = 1

#     queue = deque()
#     queue.append((0, 0))

#     while queue:
#         x, y = queue.popleft()

#         for dx, dy in direction:
#             nx = x + dx
#             ny = y + dy

#             if nx >= n or ny >= n:
#                 continue

#             if metrix[nx][ny] == 0:
#                 metrix[nx][ny] = metrix[x][y] + 1
#                 queue.append((nx, ny))

#     answer = []
#     for i in range(n):
#         answer += metrix[i]
#     print(f"answer size: {len(answer)}")
#     return answer[left:right+1]

def solution(n, left, right):
    answer = []

    target = [i for i in range(1, n+1)]
    mask = [0] * n

    for i in range(n):
        target = mask_sum(mask, target)
        mask[i] = 1
        answer += target
        # print(f"target: {target}")
        # print(f"mask: {mask}")
    
    return answer[left:right+1]

def mask_sum(mask, target):

    for i in range(len(mask)):
        target[i] += mask[i]
    
    return target

if __name__ == "__main__":
    n = 10000
    left = 519995
    right = 520000
    # n = 3
    # left = 2
    # right = 5

    start = time.time()

    print(solution(n, left, right))

    print(f"time: {time.time()-start:.5f}")
