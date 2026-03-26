class Solution:
    def splitString(self, s: str) -> bool:
        current = []

        def split(idx):
            if idx == len(s):
                return len(current) >= 2
            
            for i in range(idx,len(s)):
                val = int(s[idx:i+1])
                if not current or current[-1] - 1 == val:
                    current.append(val)
                    if split(i + 1):
                        return True
                    current.pop()
            return False
        
        return split(0)
                    

