class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def is_palindrome(substring):

            left, right = 0, len(substring) - 1

            while left < right:
                if substring[left] != substring[right]:
                    return False
                left += 1
                right -= 1
            
            return True


        def backtrack(start_index, curr_path):
            # base case: if we've reached the end of the string
            if start_index == len(s):
                res.append(list(curr_path))
                return

            # explore: try every possible end_index for the current substring

            for end_index in range(start_index, len(s)):
                substring = s[start_index: end_index + 1]

                if is_palindrome(substring):
                    curr_path.append(substring)
                    backtrack(end_index + 1, curr_path)
                    curr_path.pop()




        backtrack(0, [])

        return res