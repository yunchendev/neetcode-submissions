class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)

        for from_airport, to_airport in tickets:
            adj[from_airport].append(to_airport)
        
        for airport in adj:
            adj[airport].sort()

        itin = []
        def dfs(airport):
            while adj[airport]:
                # grab the first flight
                next_dest = adj[airport].pop(0)

                dfs(next_dest)

            itin.append(airport)

        dfs('JFK')
        
        return itin[::-1]