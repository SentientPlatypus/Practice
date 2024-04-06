class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        validmap = {}
        count = 0
        i = 0
        stopindex = len(s)
        while i < stopindex:
            c = s[i]
            if c == '(':
                count += 1
                validmap[i] = count
            elif c == ')':
                count -= 1
                if count < 0:
                    s = s[:i] + s[i+1:]  # Remove ')' from string
                    stopindex -= 1  # Adjust stopindex as the string length has decreased
                    i -= 1  # Adjust index to recheck the current position
                    count += 1
                else:
                    validmap[i] = count
            i += 1


        i = len(s) - 1
        count = 0
        stopindex = 0
        while i >= stopindex:
            c = s[i]
            if c == ')':
                count += 1
                validmap[i] = count
            elif c == '(':
                count -= 1
                if count < 0:
                    s = s[:i] + s[i+1:]  
                    count += 1
                else:
                    validmap[i] = count
            i -= 1
        return s        



        

        