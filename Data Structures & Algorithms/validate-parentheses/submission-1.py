class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in closeToOpen.keys():
                if not stack or stack.pop() != closeToOpen[char]:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
