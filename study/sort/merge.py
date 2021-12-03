def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_list = arr[:mid]
    right_list = arr[mid:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    
    return merge(left_list, right_list)

def merge(left, right):
    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0 :
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    return result



if __name__ == "__main__":
    arr = [9, 4, 3, 5, 6, 21, 12, 2]
    print(merge_sort(arr))