class Solution:
    def rotatedDigits(self, N: int) -> int:
        PAIRS = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6}
        stack = []
        for num in range(N + 1):
            digits = ""
            valid = True
            for n in [i for i in list(str(num))]:
                if int(n) not in list(PAIRS.keys()):
                    valid = False
                else:
                    digits += str(PAIRS[int(n)])
            if valid and num != int(digits):
                stack.append(int(digits))
        return len(stack)
