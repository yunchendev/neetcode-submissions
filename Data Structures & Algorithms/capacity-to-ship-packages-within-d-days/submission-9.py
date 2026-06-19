class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights) # upper bound can probably be optimized TODO
        while left < right:
            mid = (left + right) // 2 # capacity
            need_days = 0
            running_sum = 0
            for weight in weights:
                running_sum += weight
                if running_sum > mid:
                    need_days += 1
                    running_sum = weight
            need_days += 1
            if need_days <= days:
                right = mid
            else:
                left = mid + 1
        return left
            