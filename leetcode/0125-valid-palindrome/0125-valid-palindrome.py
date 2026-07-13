class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for x in s:
            if x.islower() or x.isupper():
                new += x.lower()
            if x.isdigit():
                new += x
        front = new
        back = new[::-1]
       
        return front == back