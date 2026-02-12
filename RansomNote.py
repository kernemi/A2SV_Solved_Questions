class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        A = Counter(ransomNote)
        B = Counter(magazine)
        for i in A:
            if A[i] > B[i]:
                return False
        return True
