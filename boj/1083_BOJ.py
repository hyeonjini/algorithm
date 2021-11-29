"""
소트
"""
import sys
input = sys.stdin.readline

def solution(n, arr, s):

    sorted_arr = sorted(arr, reverse=True)
    i = 0
    start = 0
    k = 0
    while s > 0:
        
        
        # print(arr)
        max_index = arr.index(sorted_arr[i])
        # print('max:', sorted_arr[i], 'index:', max_index, 's:', s)
        k = 0
        for d in range(max_index -1 , -1, -1):
            if arr[d] > arr[max_index]:
                break
            k += 1
        # print('k', k)
        if k <= s and max_index >= 0:
            j = max_index
            while j > 0 and (arr[j-1] < arr[j]):
                arr[j - 1], arr[j] = arr[j], arr[j-1]
                s -= 1
                j -= 1
            
        i += 1
    # answer = ''
    # for a in arr:
    #     answer += str(a)
    
    answer = ' '.join(list(map(str, arr)))
    return answer

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    s = int(input())
    print(solution(n, arr, s))