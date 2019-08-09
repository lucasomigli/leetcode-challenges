class Solution:
    def reverse(self, x: int) -> int:
        dash = '-' if x < 0 else ''
        res = dash + ''.join(list(reversed(list(str(abs(x)))))).lstrip("0")
        return res if x != 0 and abs(int(res)) <= pow(2, 31) else 0
