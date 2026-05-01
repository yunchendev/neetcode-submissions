class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {i:[] for i in range(1, n + 1)}
        visited = {}
        
        min_heap = [(0, k)]
        for u, v, w in times:
            adj[u].append((v, w))

        print(adj)

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited[node] = time

            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        if len(visited) == n:
            return max(visited.values())
        

        return -1