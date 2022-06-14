def solution(n):
    answer = 0
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False

    # 에라토테네스의 체
    for i in range(2, n + 1):
        if prime[i]:
            answer += 1
        for j in range(1, n + 1):
            if i * j > n:
                break
            prime[i * j] = False
    
    return answer


if __name__ == "__main__":
    print(solution(20))