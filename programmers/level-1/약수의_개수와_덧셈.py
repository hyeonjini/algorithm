def solution(left, right):
    return sum([divisor(num) for num in range(left, right + 1)])

def divisor(n):
    count = 0
    for i in range(1, (n + 1)):
        if n % i == 0:
            count += 1
    
    return n if count % 2 == 0 else -n

if __name__ == "__main__":
    left = 24
    right = 27

    print(solution(left, right))