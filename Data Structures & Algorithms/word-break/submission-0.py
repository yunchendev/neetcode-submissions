class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp represents whether the prefix of the string up to index i can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True

        return dp[len(s)]