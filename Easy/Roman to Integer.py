from functools import reduce


class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
        summation = int(ROMAN[s[-1]])
        for index in range(len(s)-1, 0, -1):
            a, b = (ROMAN[s[index]], ROMAN[s[index-1]])
            if a <= b:
                summation += b
            else:
                summation -= b
        return summation
