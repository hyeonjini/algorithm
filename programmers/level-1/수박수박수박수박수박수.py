def solution(n):
    answer = "수박" * 5000
    return answer[:n]

if __name__ == "__main__":
    n = 3
    print(solution(n))