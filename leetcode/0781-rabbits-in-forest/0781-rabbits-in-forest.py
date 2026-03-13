class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        check = []
        count = defaultdict(int)
        total = 0
        for i in answers:
            if i == 0:
                total += 1
                continue
            else:
                if i in check and count[i] >= i+1:
                    count[i] = 1
                    total +=(i+1)
                elif i in check and count[i] < i+1:
                    count[i] += 1
                elif i not in check:
                    count[i] += 1
                    check.append(i)
                    total += (i+1)
                
        return total
            