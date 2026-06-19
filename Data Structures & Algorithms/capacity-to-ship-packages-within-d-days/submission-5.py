class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) 
        r = res = sum(weights)

        def can_ship(capacity):
            ships, curr_capacity = 1, capacity

            for weight in weights:
                if curr_capacity - weight < 0:
                    ships += 1

                    if ships > days:
                        return False

                    curr_capacity = capacity
                
                curr_capacity -= weight

            return True

        while l <= r:
            capacity = (l + r) // 2

            if can_ship(capacity):
                res = min(res, capacity)
                r = capacity - 1

            else:
                l = capacity + 1

        return res
