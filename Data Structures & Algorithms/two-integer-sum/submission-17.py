class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hash_table:
                return [hash_table[diff], i]

            hash_table[num] = i

        print(hash_table)
        return [0,0]