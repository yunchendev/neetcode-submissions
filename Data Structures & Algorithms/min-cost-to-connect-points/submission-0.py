class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # min heap 

        min_heap = [(0, 0)]

        visited = set()
        total_cost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)

            # skip if already visited

            if i in visited:
                continue
            
            # add to mst

            visited.add(i)
            total_cost += cost

            x1, y1 = points[i]
            # add all edges from this point 

            for j in range(n):
                if not j in visited:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, j))

        return total_cost