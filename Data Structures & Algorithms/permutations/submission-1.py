class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        used = [False] * len(nums)

        def backtrack(curr_path):
            if len(curr_path) == len(nums):
                res.append(curr_path.copy())
                return
            for i in range(len(nums)):
                if used[i]: continue

                used[i] = True

                curr_path.append(nums[i])
                backtrack(curr_path)

                used[i] = False
                curr_path.pop()

        backtrack([])

        return res