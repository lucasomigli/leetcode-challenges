class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for char in s[::-1]:
            if count == 0 and char == " ":
                continue
            elif char == ' ':
                break
            count += 1
        return count
