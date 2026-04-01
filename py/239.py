class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = [(-nums[i], i) for i in range(k)]
        heapify(max_heap)

        res = [-max_heap[0][0]]

        for i in range(k, len(nums)):
            heappush(max_heap, (-nums[i], i))

            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
  
            res.append(-max_heap[0][0])
        
        return res

            



