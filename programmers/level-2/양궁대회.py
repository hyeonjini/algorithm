def solution(n, info):
    answer = []
    ryan = [0] * len(info)
    print(f"apeach: {info}")
    for i in range(n+1): # 어피치가 맞춘 화살 개수(i) 0 <= i <= n
        print(f"현재 화살 개수: {i}")
        for k in range(11): # 양궁 점수 0 <= k < 11
            if info[k] == i and n >= info[k] + 1: # 큰 점수부터 남은 화살 n개로 쏠 수 있는 과녁 탐색
                ryan[k] = info[k] + 1
                n -= info[k] + 1 # 남은 화살 개수 감소
    print(f"ryan: {ryan}")




    exit()
    return answer

if __name__ == "__main__":
    assert solution(5, [2,1,1,1,0,0,0,0,0,0,0]) == [0,2,2,0,1,0,0,0,0,0,0]
    assert solution(1, 	[1,0,0,0,0,0,0,0,0,0,0]) == [-1]
    assert solution(9, [0,0,1,2,0,1,1,1,1,1,1]) == [1,1,2,0,1,2,2,0,0,0,0]
    assert solution(10, [0,0,0,0,0,0,0,0,3,4,3]) == [1,1,1,1,1,1,1,1,0,0,2]