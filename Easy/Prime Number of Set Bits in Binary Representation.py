class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count = 0
        for num in range(L, R+1):
            bits = bin(num).count('1')
            prime = True
            if bits == 2:
                count += 1
            elif bits > 2:
                for i in range(2, bits):
                    if bits % i == 0:
                        prime = False
                        break
                if prime == True:
                    count += 1

        return count
