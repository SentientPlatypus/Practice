class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chardict = {}
        for ch in s:
            try:
                chardict[ch] += 1
            except:
                chardict[ch] = 1
        

        for ch in t:
            try:
                chardict[ch] -= 1
                if chardict[ch] < 0:
                    return False
            except:
                return False
        
        for key in chardict.keys():
            if chardict[key] != 0:
                return False
        
        return True
            