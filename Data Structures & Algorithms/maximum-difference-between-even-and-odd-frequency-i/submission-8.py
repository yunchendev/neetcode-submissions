class Solution:
    def maxDifference(self, s: str) -> int:
        even, odd = float('inf'), float('-inf')
        letters = set(s)
        for letter in letters:
            count = s.count(letter)
            if count % 2 != 0:
                odd = max(odd, count)
            else:
                even = min(even, count)
        return odd - even