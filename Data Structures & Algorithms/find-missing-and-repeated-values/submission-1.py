class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        n = len(grid) * len(grid[0])

        freq = {}

        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1

        repeat = 0
        missing = 0

        for i in range(1, n + 1):
            if i in freq and freq[i] > 1:
                repeat = i
            
            elif i not in freq:
                missing = i

        return [repeat, missing]
