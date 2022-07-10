def solution(n):
    ans = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            n /= 2
            ans += 1

    return ans + 1

if __name__ == "__main__":
    assert solution(5) == 2
    assert solution(6) == 2
    assert solution(5000) == 5
    assert solution(1e9)
