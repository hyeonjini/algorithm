def solution(sizes):
    answer = 0
    sizes = [[min(x1, x2), max(x1, x2)] for x1, x2 in sizes]
    
    x1 = [x[0] for x in sizes]
    x2 = [x[1] for x in sizes]
    return max(x1) * max(x2)

if __name__ == "__main__":
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    print(solution(sizes))
