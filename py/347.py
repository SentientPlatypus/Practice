class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)

        mst_cmn = cntr.most_common()
        return [mst_cmn[i][0] for i in range(k)]

        
