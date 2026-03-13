class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = {}
        total = 0
        n = len(costs)
        a = 0
        b = 0

        for i in range(n):
            diff[i] = abs(costs[i][0]-costs[i][1])

        diff = dict(sorted(diff.items(),key=lambda x:x[1], reverse= True))
        atrue = True
        bTrue = True
        for i in diff:
            if min(costs[i][0],costs[i][1]) == costs[i][0] and atrue and bTrue:
                total += costs[i][0]
                a += 1
            elif min(costs[i][0],costs[i][1]) == costs[i][1] and bTrue and atrue:
                total += costs[i][1]
                b += 1
            if not atrue:
                total += costs[i][1]
                b+= 1
                
            if not bTrue:
                total += costs[i][0]
                a += 1 
            if a == n//2:
                atrue = False
                
            if b == n//2:
                bTrue = False
           
            

        return total