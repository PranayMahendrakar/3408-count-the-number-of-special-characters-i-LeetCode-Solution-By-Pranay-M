class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set(c for c in word if c.islower())
        upper = set(c for c in word if c.isupper())
        count = 0
        for c in lower:
            if c.upper() in upper:
                count += 1
        return count