class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)

        res = 0

        for word in words:
            curr_word = Counter(word)
            good = True

            for c in curr_word:
                if curr_word[c] > count[c]:
                    good = False
                    break
            
            if good:
                res += len(word)

        return res
        

        