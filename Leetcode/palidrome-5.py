class Solution: 
    def longestPalindrome(self, s):
            longest_palindrom = ''
            dp = [[0]*len(s) for _ in range(len(s))]
            #filling out the diagonal by 1
            for i in range(len(s)):
                dp[i][i] = True
                longest_palindrom = s[i]

            # filling the dp table
            for i in range(len(s)-1,-1,-1):
                for j in range(i+1,len(s)):  
                    if s[i] == s[j]:
                        if j-i ==1 or dp[i+1][j-1] is True:
                            dp[i][j] = True
                            if len(longest_palindrom) < len(s[i:j+1]):
                                longest_palindrom = s[i:j+1]

            return longest_palindrom

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            if s is "":
                return False
            for i in range(len(s)//2):
                if s[i] != s[-1-i]:
                    return False
            return True

        common_subs = {}

        if s is "":
            return ""

        for i in range(len(s)):
            for j in range(1, len(s)+1):
                if isPalindrome(s[i:j]):
                    common_subs[s[i:j]] = len(s[i:j])

        return max(common_subs, key=common_subs.get)


"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):        
            odd  = self.findPali(s, i, i)
            even = self.findPali(s, i, i+1)

            res = max(res, odd, even, key=len)
        return res

    # starting at l,r expand outwards to find the biggest palindrome
    def findPali(self, s, l, r):    
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
"""