class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        


        dict_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in dict_map:
                return [dict_map[diff], i]
            else:
                dict_map[num] = i

