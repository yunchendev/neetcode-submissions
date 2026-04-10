class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return

        ROWS, COLS = len(rooms), len(rooms[0])

        q = deque()

        # add all the gates to the queue to start multi-source bfs

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                # if neighbor is in bounds and is empty room

                if (0 <= nr < ROWS and 0 <= nc < COLS and rooms[nr][nc] == 2147483647):
                    
                    rooms[nr][nc] = rooms[r][c] + 1

                    q.append((nr, nc))
