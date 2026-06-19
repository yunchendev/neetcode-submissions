class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_capacity, max_capacity = max(weights), sum(weights)

        while min_capacity < max_capacity:
            trial_capacity = (min_capacity + max_capacity) // 2

            days_needed = 0
            current_day_load = 0

            for weight in weights:
                current_day_load += weight
                if current_day_load > trial_capacity:
                    days_needed += 1
                    current_day_load = weight  # Start the next day with this package

            days_needed += 1  # Include the final day in progress

            # Adjust search range based on whether we met the deadline
            if days_needed <= days:
                max_capacity = trial_capacity  # Try to find a smaller valid capacity
            else:
                min_capacity = trial_capacity + 1  # Increase capacity; current is too small

        return min_capacity