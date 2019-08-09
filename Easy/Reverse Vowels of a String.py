class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AaEeIiOoUu"
        filtered = [v for v in s if v in vowels]
        st = ""
        for char in s:
            if char in vowels:
                char = filtered.pop()
            st += char
        return st
