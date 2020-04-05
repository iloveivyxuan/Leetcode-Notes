class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s

        n = len(s) - 1
        dp = [[0 for x in range(n+1)] for y in range(n)]
        res = s[0]

        for i in range(n - 1, -1, -1):
            for j in range(i, n + 1):
                if s[i] == s[j] and ((j - i < 3) or dp[i+1][j-1]):
                    dp[i][j] = True
                else:
                    dp[i][j] = False

                if dp[i][j] and j+1 - i > len(res):
                    res = s[i:j+1]

        return res
