class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) < 2:
            return len(people)
        people.sort()
        p = 0
        n= len(people)
        q = n-1
        while p < q:
            if people[p] + people[q] <= limit:
                n -= 1
                p += 1
                q -= 1
            else:
                q -= 1
        return n
            
        
