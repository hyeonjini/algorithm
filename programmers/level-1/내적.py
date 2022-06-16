def solution(a, b):
    
    return sum([_a * _b for _a, _b in zip(a, b)])

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    b = [-3, -1, 0, 2]
    print(solution(a, b))