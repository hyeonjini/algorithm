from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        pivot = len(nums) // 2

        visited = [True] * len(nums)

        while pivot > 0 and pivot < len(nums) - 1:

            left = sum(nums[:pivot])
            right = sum(nums[pivot+1:])
            
            visited[pivot] = False

            if left == right:
                return pivot

            if left < right:
                if not visited[pivot + 1]:
                    break
                pivot += 1


            else:
                if not visited[pivot - 1]:
                    break
                pivot -= 1

        
        return -1


if __name__ == "__main__":
    solution = Solution()

    assert solution.pivotIndex([1,7,3,6,5,6]) == 3
    assert solution.pivotIndex([1,2,3]) == -1

    assert solution.pivotIndex([-1, -1, -1, -1, -1, -1]) == -1