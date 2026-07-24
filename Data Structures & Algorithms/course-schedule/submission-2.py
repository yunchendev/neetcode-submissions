class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        adj = {i: [] for i in range(num)}

        for c,p in pre:
            adj[c].append(p)
        
        visit = [0] * num

        def dfs(c):
            if visit[c] == 1:
                return False
            if visit[c] == 2:
                return True
            
            visit[c] = 1
            for p in adj[c]:
                if not dfs(p):
                    return False
            
            visit[c] = 2
            return True
        
        for c in range(num):
            if not dfs(c):
                return False
                
        return True