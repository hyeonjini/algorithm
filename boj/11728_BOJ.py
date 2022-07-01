import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    # arr1_idx = 0
    # arr2_idx = 0
    
    # result = [0]
    
    # while arr1_idx < len(arr1) and arr2_idx < len(arr2):

    #     if arr1[arr1_idx] <= arr2[arr2_idx]:
    #         result.append(arr1[arr1_idx])
    #         arr1_idx += 1
    #     else:
    #         result.append(arr2[arr2_idx])
    #         arr2_idx += 1
    
    # result += arr1[arr1_idx:]
    # result += arr2[arr2_idx:]
    
    # for r in result:
    #     print(r, end=" ")