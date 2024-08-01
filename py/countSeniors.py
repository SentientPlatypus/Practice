class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count = 0
        for s in details:
            count += int(s[11:13]) > 60
        return count
        