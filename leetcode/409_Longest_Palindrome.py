from collections import defaultdict, Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # ingredient = defaultdict(int)
        # for item in s:
        #     ingredient[item] += 1
        ingredient = Counter(s)
        answer = 0
        odd = False
        for value in ingredient.values():
            answer += (value // 2) * 2
            if value % 2 != 0:
                odd = True

        return answer + odd


if __name__ == "__main__":

    solution = Solution()

    assert solution.longestPalindrome("abccccdd") == 7
    assert solution.longestPalindrome("a") == 1
    assert solution.longestPalindrome("bb") == 2
    assert solution.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth") == 983