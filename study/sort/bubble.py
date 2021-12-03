def bubble_sort(arr):
    n = len(arr)
    print(arr)
    for i in range(n):
        for j in range((n-1) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [9, 4, 3, 5, 6, 21, 12, 2]
    print(bubble_sort(arr))

# O(n**2)