class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)

        for i in range(len(s)):
            
            if s[i] == "6":
                s = s[:i] + "9" + (s[i + 1:] if i != len(s) - 1 else "")
                break
        
        return int(s)