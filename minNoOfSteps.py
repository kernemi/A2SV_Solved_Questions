class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s1 = Counter(s)
        s2 = Counter(t)
        n = 0
        for key in s2:
            if key in s1:
                if s2[key] > s1[key]:
                    n += (s2[key] - s1[key])
            else:
                n += s2[key]
        return n
