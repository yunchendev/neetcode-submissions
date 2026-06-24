class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last element and move backwards
        for i in range(len(digits) - 1, -1, -1):
            # If the digit is less than 9, just increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, it becomes 0 (carry moves left)
            digits[i] = 0
            
        # If we exit the loop, it means we had a carry out of the front (e.g., 99 -> 100)
        return [1] + digits