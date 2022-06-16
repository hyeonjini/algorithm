def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i

if __name__ == "__main__":
    n = 12
    print(solution(n))