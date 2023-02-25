class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=lambda x:len(x))
        strIndex = 0
        while strIndex <= len(strs[0]) - 1:
            works = True
            for word in strs:
                if word[strIndex] == strs[0][strIndex]:
                    continue
                works = False
                break
            if not works:
                break
            else:
                strIndex += 1
        return strs[0][:strIndex]




print(Solution.longestCommonPrefix(
    Solution,
    [
    "zlower",
    "flow",
    "floght"
]))


