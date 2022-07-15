class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        ingredient_s = {}
        ingredient_t = {}
        for _s, _t in zip(list(s), list(t)):
            if _s not in ingredient_s.keys():
                ingredient_s[_s] = len(ingredient_s.keys())
            
            if _t not in ingredient_t.keys():
                ingredient_t[_t] = len(ingredient_t.keys())

            _s = ingredient_s[_s]
            _t = ingredient_t[_t]
            
            if _s != _t:
                return False

        return True

if __name__ == "__main__":

    solution = Solution()

    assert solution.isIsomorphic("egg", "add") == True
    assert solution.isIsomorphic("foo", "bar") == False
    assert solution.isIsomorphic("paper", "title") == True

