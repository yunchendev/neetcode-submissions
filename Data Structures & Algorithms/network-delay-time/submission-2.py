class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0
        min_heap = [(0, k)]

        while min_heap:
            curr_time, node = heapq.heappop(min_heap)

            if distances[node] < curr_time:
                continue

            for neighbor, travel_time in adj[node]:
                new_time = travel_time + curr_time

                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        max_value = max(distances.values())

        return max_value if max_value != float('inf') else -1

