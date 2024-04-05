class Solution:
    def makeGood(self, s: str) -> str:
        s_list = list(s)

        i = 1
        while i < len(s_list):
            if s_list[i].lower() == s_list[i - 1].lower() and s_list[i] != s_list[i - 1]:
                s_list.pop(i)
                s_list.pop(i - 1)
                i = 1
            else:
                i += 1
        
        return "".join(s_list)
            
