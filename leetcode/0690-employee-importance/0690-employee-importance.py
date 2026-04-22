"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def solve(idd):
            info = dicts[idd]
            total = info.importance

            for i in info.subordinates:
                total += solve(i)
            
            return total
        
        dicts = {e.id:e for e in employees}
        return solve(id)
        