class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) / k
        nums.sort(reverse=True)
        buckets = [0] * k
        
        def backtrack(curi):
            if curi == len(nums):
                return True
                
            for i in range(k):
                if buckets[i] + nums[curi] <= target:
                    buckets[i] += nums[curi]
                    
                    if backtrack(curi + 1):
                        return True
                        
                    buckets[i] -= nums[curi]
                    
                if buckets[i] == 0:
                    break
                    
            return False
            
        return backtrack(0)
