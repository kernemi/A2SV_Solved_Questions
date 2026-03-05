class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0]*len(s)
        for l,r,k in shifts:
            shift[l] += 1 if k == 1 else -1
            if r + 1 < len(shift):
                shift[r+1] -= 1 if k == 1 else -1
        for i in range(1,len(s)):
            shift[i] += shift[i-1]
        new = ""
        for i in range(len(s)):
            chars = chr((ord(s[i]) - ord('a') + shift[i]) % 26 + ord('a'))
            new += chars
        return new
