from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        left = 0
        right = sum(nums)

        pre_pivot = 0
        for i in range(len(nums)):

            right -= nums[i]
            left += pre_pivot

            if left == right:
                return i

            pre_pivot = nums[i]

        return -1

            


if __name__ == "__main__":
    solution = Solution()

    assert solution.pivotIndex([1,7,3,6,5,6]) == 3
    assert solution.pivotIndex([1,2,3]) == -1

    assert solution.pivotIndex([-1, -1, -1, -1, -1, -1]) == -1