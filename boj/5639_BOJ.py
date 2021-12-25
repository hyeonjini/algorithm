"""
이진 검색 트리
"""
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def solution(nums):
    if len(nums) <= 1:
        return nums
    
    for i in range(1, len(nums)):
        if nums[i] > nums[0]:
            return solution(nums[1:i]) + solution(nums[i:]) + [nums[0]]

    return solution(nums[1:]) + [nums[0]]

if __name__ == "__main__":
    nums = []
    while True:
        try:
            nums.append(int(input()))
        except:
            break
    
    nums = solution(nums)
    for num in nums:
        print(num)
    