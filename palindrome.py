class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = 0
        original = x
        while x > 0:
            digit = x % 10
            reversed = (reversed*10) + digit 
            x//=10
        return original == reversed
