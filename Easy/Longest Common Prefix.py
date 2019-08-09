class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 0:
            min_length_word = min(strs, key=len)
            for length in range(len(min_length_word), 0, -1):
                chunk = min_length_word[0:length]
                check = list(map(lambda word: chunk in word[0:length], strs))
                if all(checks == True for checks in check):
                    return chunk
        return ""
