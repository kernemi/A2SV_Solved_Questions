class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = list(map(str,s.split()))
        dicts = {}
        samples = []
        if len(pattern) != len(words):
            return False
        for i in range(len(words)):
            if pattern[i] not in dicts and words[i] not in samples:
                dicts[pattern[i]] = words[i]
                samples.append(words[i])
            elif pattern[i] not in dicts and words[i] in samples:
                return False
            else:
                if dicts[pattern[i]] != words[i]:
                    return False
        return True
