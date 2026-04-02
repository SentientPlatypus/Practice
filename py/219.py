class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()
        l = 0

        for r in range(len(nums)):
            nxt = nums[r]

            if nxt in win:
                return True
            
            win.add(nxt)

            if r - l + 1 <= k:
                continue
            
            win.remove(nums[l])
            l += 1
        return False
            
