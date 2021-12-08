import sys

input = sys.stdin.readline

def solution(n, k, numbers):
    
    stack = []
    s = k
    for i in range(n):
        while stack and k > 0:
            if stack[-1] < numbers[i]:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(numbers[i])
    # print('stack:', stack)
    answer = ''.join(list(map(str, stack[:(n-s)])))
    
    return answer if answer != '' else 0

if __name__ == "__main__":
    n, k = map(int, input().split())
    numbers = list(map(int, (input().strip())))
    print(solution(n, k, numbers))