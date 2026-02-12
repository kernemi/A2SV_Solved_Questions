class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        formats = defaultdict(int)
        
        for x,y in zip(s1,s2):
            formats[x + y] += 1
        xy = formats["xy"]
        yx = formats["yx"]
        if (xy + yx) % 2 == 1:
            return -1
        
        return (xy // 2) + (yx // 2) + (xy % 2) + (yx % 2)
