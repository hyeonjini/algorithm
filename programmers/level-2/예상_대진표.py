def solution(n,a,b):
    answer = 0

    if b < a: # b가 무조건 큰 수
        a, b = b, a
    
    while True:
        # print(f"a: {a}, b: {b}")
        answer += 1
        if a + 1 == b and b % 2 == 0:
            break
        a = (a + 1) // 2
        b = (b + 1) // 2

        
    return answer

if __name__ == "__main__":
    assert solution(8, 4, 7) == 3
    assert solution(8, 1, 8) == 3
    assert solution(16, 8, 11)