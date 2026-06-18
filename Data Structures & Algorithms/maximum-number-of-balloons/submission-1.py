class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_freq = Counter(text)
        balloon = Counter("balloon")

        res = len(text)

        for c in balloon:
            res = min(res, text_freq[c] // balloon[c])

        return res