def solution(arr1, arr2):
    
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):

        for j in range(len(arr2[0])):
            for n, m in zip(arr1[i], [arr[j] for arr in arr2]):
                answer[i][j] += n * m

    return answer

if __name__ == "__main__":
    assert solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]) == [[15, 15], [15, 15], [15, 15]]
    assert solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]) == [[22, 22, 11], [36, 28, 18], [29, 20, 14]]