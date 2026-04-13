class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()

        ROWS, COLS = len(grid), len(grid[0])
        fresh_count = 0

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        if fresh_count == 0:
            return 0

        minutes = 0

        while queue and fresh_count > 0:
            minutes += 1
            # process all fruit currently in the queue for this minute

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        # infect fruit

                        grid[nr][nc] = 2

                        fresh_count -=1 

                        queue.append((nr, nc))

        return minutes if fresh_count == 0 else -1