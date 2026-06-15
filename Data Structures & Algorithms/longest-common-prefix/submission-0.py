class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""

        for i in range(len(strs[0])):
            letter = strs[0][i]

            for word in strs:
                if i >= len(word) or letter != word[i]:
                    return prefix
            
            prefix += letter

        return prefix