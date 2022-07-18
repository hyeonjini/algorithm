from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_buy = 1e9

        for price in prices:
            min_buy = min(min_buy, price)
            max_profit = max(max_profit, price-min_buy)

        return max_profit


if __name__ == "__main__":
    solution = Solution()

    # assert solution.maxProfit([7,1,5,3,6,4]) == 5
    # assert solution.maxProfit([7,6,4,3,1]) == 0
    # assert solution.maxProfit([2,4,1]) == 2
    assert solution.maxProfit([1,2]) == 1