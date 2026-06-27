class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)

        res = 0

        for word in words:
            curr_word = Counter(word)
            curr_len = 0

            for c in curr_word:
                if curr_word[c] <= count[c]:
                    curr_len += curr_word[c]
            
            if curr_len == len(word):
                res += len(word)

        return res
        