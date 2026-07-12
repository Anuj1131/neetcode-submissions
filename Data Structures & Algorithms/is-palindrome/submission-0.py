class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = 0
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]