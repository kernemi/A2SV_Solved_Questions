class Solution:
    def frequencySort(self, s: str) -> str:
        x = list(s)
        x.sort()
        s = "".join(x)
        charCount = Counter(s)
        charCount = sorted(charCount.items(), key=lambda x:x[1], reverse =True)
        result = []
        for ch, freq in charCount:
            result.append(ch*freq)
        ans = "".join(result)
        return ans
