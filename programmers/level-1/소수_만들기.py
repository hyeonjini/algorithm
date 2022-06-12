from itertools import combinations
def solution(nums):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for candi in list(combinations(nums, 3)):
        if is_prime(sum(candi)):
            answer += 1


    return answer
def is_prime(n):

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
    
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(solution(nums))