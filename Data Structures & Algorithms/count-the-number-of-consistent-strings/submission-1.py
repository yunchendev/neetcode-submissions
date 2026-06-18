class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allowed = set(allowed)

        res = 0

        for word in words:
            if all([ch in allowed for ch in word]):
                res += 1

        return res