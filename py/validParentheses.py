class Solution:
    def isValid(self, s: str) -> bool:
        p_count = 0
        b_count = 0
        s_count = 0

        for char in s:
            if char == "(":
                p_count += 1
            elif char == ")":
                p_count -= 1
            elif char == "[":
                s_count += 1
            elif char == "]":
                s_count -= 1
            elif char == "{":
                b_count += 1
            elif char == "}":
                b_count -= 1
            if p_count < 0 or s_count < 0 or b_count < 0:
                return False
            
            if (len(set([p_count, s_count, b_count]))!=1) and (p_count != 0 and s_count != 0 and b_count != 0):
                return False

        if p_count == 0 and s_count == 0 and b_count == 0:
            return True
        return False

m = Solution()
print(m.isValid( "({)}"))