class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if sum(skill) % (n//2) != 0:
            return -1
        tempo = {}
        num = sum(skill) // (n//2)
        skill.sort()
        p = 0
        q = n-1
        result = 0
        while p < q:
            if skill[p] + skill[q] == num:
                result += (skill[p] * skill[q])
                p += 1
                q -= 1
            else:
                return -1
        return result
       
