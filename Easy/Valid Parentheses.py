class Solution:
    def isValid(self, s: str) -> bool:
        BRACKETS = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for char in s:
            if char in BRACKETS:
                stack.append(BRACKETS[char])
            else:
                if not stack or stack.pop() != char:
                    return False

        return not stack
