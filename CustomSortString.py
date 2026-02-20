class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""
        extra = ""
        s = Counter(s)
        for i in order:
            if i in s:
                result += i*(s[i])
                del s[i]
        s = sorted(s.items())
        for i,y in s:
            extra += (i*y)
        result += extra
        return result
        
