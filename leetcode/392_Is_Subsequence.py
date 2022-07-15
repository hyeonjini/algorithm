
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        k = 0
        for _s in s:
            k = t.find(_s)
            if k == -1:
                return False
            t = t[k+1:]
        return True

if __name__ == "__main__":
    solution = Solution()

    assert solution.isSubsequence("abc", "ahbgdc") == True
    assert solution.isSubsequence("axc", "ahbgdc") == False
    assert solution.isSubsequence("acb", "ahbgdc") == False
    assert solution.isSubsequence("aaaaaa", "bbaaaa") == False