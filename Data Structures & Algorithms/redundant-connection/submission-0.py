class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        

        adj = defaultdict(list)

        def dfs(start, target, visited):
            if start == target:
                return True

            visited.add(start)

            for node in adj[start]:
                if node not in visited:
                    if dfs(node, target, visited):
                        return True
            return False

        for u, v in edges:
            visited = set()

            if u in adj and v in adj and dfs(u, v, visited):
                return [u, v]

            adj[u].append(v)
            adj[v].append(u)

        

        

        
        
