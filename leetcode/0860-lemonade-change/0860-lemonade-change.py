class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = {5:0,10:0}
        for i in bills:
            if i == 5:
                counts[i] += 1
            elif i == 10:
                if counts[5] == 0:
                    return False
                else:
                    counts[i] += 1
                    counts[5] -= 1
            else:
                if counts[10] >= 1 and counts[5] >= 1:
                    counts[10] -= 1
                    counts[5] -= 1
                elif counts[5] >= 3:
                    counts[5] -= 3
                else:
                    return False
        return True
                  
