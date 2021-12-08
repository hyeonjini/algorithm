def insertion_sort(arr):
    n = len(arr)
    print(arr)
    
    for i in range(1, n):
        temp = arr[i]
        prev = i - 1

        while prev >= 0 and arr[prev] > temp: # prev는 n부터 0까지 탐색, temp가 들어갈 위치면 break
            arr[prev + 1] = arr[prev]
            prev -= 1

        arr[prev + 1] = temp # temp가 들어갈 위치에 삽입

    return arr

if __name__ == "__main__":
    arr = [9, 4, 3, 5, 6, 21, 12, 2]
    print(insertion_sort(arr))