class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[r])
            max_length = max(max_length, r - left + 1)

        return max_length
