"""
달팽이
"""
def solution(n):
    answer = []
    temp = [[] for _ in range(n)]

    return answer

def front(start, arr, n):
    for i in range(start, start + n):
        arr[i].append(i)

if __name__ == "__main__":
    n = 4
    # n = 5
    # n = 6
    print(solution(n))