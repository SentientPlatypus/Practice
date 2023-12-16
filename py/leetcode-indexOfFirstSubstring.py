class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            for k in range(len(needle)):
                if i + k >= len(haystack) or haystack[i + k] != needle[k]:
                    break
                if k == len(needle) - 1 and haystack[i + k] == needle[k]:
                    return i
        return -1
        