# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(serlf, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        if not pairs:
            return res
        for i in range(1, len(pairs)):
            j = i - 1
            res.append(pairs.copy())
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
        res.append(pairs.copy())
        return res