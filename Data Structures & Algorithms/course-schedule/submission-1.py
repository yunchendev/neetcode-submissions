class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        current_path = set()
        adj = {i: [] for i in range(numCourses)}
        def dfs(course):
            if course in current_path:
                return False

            if course in visited:
                return True

            current_path.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False

            current_path.remove(course)

            visited.add(course)
            return True

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        for i in range(numCourses):
           
            if not dfs(i):
                return False

        return True
