class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)):
            s.insert(i, s.pop())
