def solution(numbers):
    return sum([num for num in range(10) if num not in numbers])

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 6, 7, 8, 0]
    print(solution(numbers))