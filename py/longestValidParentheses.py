class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        m = 0
        n = len(s)

        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            else:
                if st:
                    if s[st[-1]] == '(':
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)
        
        if not st: return n
        a = n
        b = 0
        while st:
            b = st[-1]
            st.pop()
            m = max(m, a - b - 1)
            a = b
        m = max(m, a)
        return m
            

                        