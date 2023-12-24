class Solution:
    def minOperations(self, s: str) -> int:
        changes_01 = 0  
        changes_10 = 0  

        for i in range(len(s)):
            if i % 2 == 0 and s[i] != '0':
                changes_01 += 1
            elif i % 2 == 1 and s[i] != '1':
                changes_01 += 1

        for i in range(len(s)):
            if i % 2 == 0 and s[i] != '1':
                changes_10 += 1
            elif i % 2 == 1 and s[i] != '0':
                changes_10 += 1

        return min(changes_01, changes_10)