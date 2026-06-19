class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s).values()

        odd_freqs = [f for f in freq if f % 2 != 0]
        even_freqs = [f for f in freq if f % 2 == 0]

        return max(odd_freqs) - min(even_freqs)