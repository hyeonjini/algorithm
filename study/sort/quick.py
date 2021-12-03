def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == "__main__":
    arr = [9, 4, 3, 5, 6, 21, 12, 2]
    print(quick_sort(arr))