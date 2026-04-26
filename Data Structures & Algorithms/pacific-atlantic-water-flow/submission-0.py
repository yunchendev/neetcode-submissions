class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # need to reach the top left and bottom right sides
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()

        res = []
        def dfs(r, c, visit_set, prev_height):
            if r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prev_height or (r, c) in visit_set:
                return
            visit_set.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit_set, heights[r][c])


        for c in range(cols):
            # Top row (Pacific)
            dfs(0, c, pac, heights[0][c])
            # Bottom row (Atlantic)
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            # left column (Pacific)
            dfs(r, 0, pac, heights[r][0])
            # right column (Atlantic)
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        return [list(cell) for cell in (atl & pac)]