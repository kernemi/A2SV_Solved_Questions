class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        w1 = Counter(word1)
        w2 = Counter(word2)

        for i in w1:
            if i not in w2:
                return False
        w1freq = sorted(w1.values())
        w2freq = sorted(w2.values())
        return w1freq == w2freq 
