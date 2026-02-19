class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        n = len(piles)//3
        maxchoice = 0
        k = 1
        for i in range(n):
            maxchoice += piles[k]
            k += 2
        return maxchoice
