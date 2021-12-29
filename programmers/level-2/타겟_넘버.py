"""
타겟 넘버
"""
answer = 0
def solution(numbers, target):

    dfs(0, 0, numbers, target)

    return answer

def dfs(total, current, numbers, target):
    global answer

    if current == len(numbers):
        if total == target:
            answer += 1
        return total
        
    dfs(total - numbers[current], current + 1, numbers, target)
    dfs(total + numbers[current], current + 1, numbers, target)
    

if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3

    print(solution(numbers, target))