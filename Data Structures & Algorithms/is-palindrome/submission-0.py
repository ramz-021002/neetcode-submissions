class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(char.lower() for char in s if char.isalnum())

        rev = word[::-1]

        if word == rev:
            return True
        else:
            return False