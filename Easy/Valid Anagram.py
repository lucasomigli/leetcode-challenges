class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stack = []
        t = list(t)
        if len(s) != len(t):
            return False
        else:
            for char in s:
                stack.append(char)
                if (char in t):
                    stack.remove(char)
                    t.remove(char)

        return len(stack) == 0
