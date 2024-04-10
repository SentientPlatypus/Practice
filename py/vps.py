class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mapping = {
            '(':')',
            '[':']',
            '{':'}'
        }

        for c in s:
            if c in ['(', '[', '{']:
                st.append(c)
            else:
                if st:
                    if st[-1] in ['(', '[', '{'] and mapping[st[-1]] == c:
                        st.pop()
                    else:
                        return False
                else:
                    return False
        
        return True if not st else False
        