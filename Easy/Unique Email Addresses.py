class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        lis = []
        for mail in emails:
            st = []
            plus = 0
            at = 0
            for char in mail:
                at += 1 if char == '@' else at
                if char == '+':
                    plus += 1
                if at > 0:
                    st.append(char)
                elif char not in ".+" and plus == 0:
                    st.append(char)

            lis.append(''.join(st))

        return len(set(lis))
