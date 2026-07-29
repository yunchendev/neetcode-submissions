# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        mid = (r + l) // 2
        print(mid)
        guess_num = guess(mid)
        print(guess_num)

        while guess_num != 0:
            if guess_num == -1:
                r = mid - 1
                
            if guess_num == 1:
                l = mid + 1

            mid = (r + l) // 2
            
            guess_num = guess(mid)

        return mid

        

        