class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        items = [symbols[item] for item in list(s)]
        
        answer = 0
        while items:
            current = items.pop(0)
            if len(items) > 0 and current < items[0]:
                answer += items.pop(0) - current
                continue
            answer += current
        
        return answer


if __name__ == "__main__":
    solution = Solution()
    assert(solution.romanToInt("III")) == 3
    assert(solution.romanToInt("LVIII")) == 58
    assert(solution.romanToInt("MCMXCIV")) == 1994