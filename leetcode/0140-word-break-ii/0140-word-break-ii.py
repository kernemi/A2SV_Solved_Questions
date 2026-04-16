class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []

        def solve(idx,path):
            if idx == len(s):
                result.append(' '.join(path))
                return
            for i in range(idx,len(s)):
                word = s[idx:i+1]
                if word in wordDict:
                    path.append(word)
                    solve(i+1,path)
                    path.pop()
            
        solve(0,[])
        return result