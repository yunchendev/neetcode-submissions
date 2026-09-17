class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_table = {}

        for s in strs:
            key = [0] * 26
            for c in s: 
                key[ord(c) - ord('a')] += 1

            tuple_key = tuple(key)
            if tuple_key not in hash_table:
                hash_table[tuple_key] = []

            hash_table[tuple_key].append(s)

        return list(hash_table.values())

            