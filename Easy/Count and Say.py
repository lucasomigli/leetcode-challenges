class Solution:
    def countAndSay(self, n: int) -> str:
        DICT = {1: '1'}
        for i in range(1, n):
            if i == n:
                break
            st = DICT[i]
            stack = st[0]
            count = 0
            PAIRS = []
            for index, val in enumerate(st):
                if (val == stack):
                    count += 1
                else:
                    stack = val
                    PAIRS.append([st[index-1], count])
                    count = 1
            PAIRS.append([st[-1], count])

            DICT[i+1] = ''.join([str(i[1]) + str(i[0]) for i in PAIRS])

        return DICT[n]
