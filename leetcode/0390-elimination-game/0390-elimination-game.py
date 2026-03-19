class Solution:
    def lastRemaining(self, n: int) -> int:

        def winner(n,move):

            if n == 1:
                return 1
            
            if move == "left":
                return 2 * winner(n//2,"right")
            else:
                if n % 2 == 0:
                    return 2 * winner(n//2,"left") -1
                else:
                    return 2 * winner(n//2,"left")
            

        return winner(n,"left")
      