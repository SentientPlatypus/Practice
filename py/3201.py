
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        res = 0
        pattern_list = [[0, 0], [0, 1], [1, 0], [1, 1]]
        for pattern in pattern_list:
            cnt = 0 
            for num in nums:
                if num % 2 == pattern[cnt % 2]:
                    cnt += 1
            res = max(res, cnt)
        return res