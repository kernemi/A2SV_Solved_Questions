class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        answer = (k + self.findTheWinner(n-1,k)) % n
        return n if answer == 0 else answer