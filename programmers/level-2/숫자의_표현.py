def solution(n):
    answer = 0

    arr = [i for i in range(1, n + 1)]

    left = 0 
    right = 0

    while left < n:

        seq_sum = sum(arr[left:right+1])
        
        if seq_sum == n:
            answer += 1
        
        if seq_sum < n:
            right += 1

        else:
            left += 1

    return answer


if __name__ == "__main__":
    assert solution(15) == 4