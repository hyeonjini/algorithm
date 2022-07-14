
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            answer.append(sum)

        return answer

if __name__ == "__main__":
    solution = Solution()

    assert solution.runningSum([1,2,3,4]) == [1,3,6,10]
    assert solution.runningSum([1,1,1,1,1]) == [1,2,3,4,5]
    assert solution.runningSum([3,1,2,10,1]) == [3,4,6,16,17]