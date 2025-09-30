class Solution:
    def gcd(x, y):
        if x > y:
            return gcd(y, x)
        if y == 0:
            return x
        return gcd(y, x % y)

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        while nums != self.helper(nums.copy()):
            nums = self.helper_faster(nums.copy())
        return nums

    def helper(self, nums:List[int]):
        n = len(nums)

        processed = []

        for i in range(1, n):
            x = nums[i - 1]
            y = nums[i]

            gcd = Solution.gcd(x,y)                                                                                                             
            if gcd != 1: #not coprime
                lcm = x * y // gcd

                nums[i - 1] = 0
                nums[i] = lcm
            else:
                continue
        
        print(nums)
        return list(filter(lambda x : x != 0, nums))
    

    def helper_faster(self, nums:list[int]):
        stack = []

        for num in nums:
            while stack and Solution.gcd(stack[-1], num) != 1:
                gcd = Solution.gcd(stack[-1], num)
                num = (stack.pop() * num) // gcd
            stack.append(num)
        
        return stack 


if __name__ == "__main__":
    s = Solution()

    inpt = [6,4,3,2,7,6,2]

    print(s.replaceNonCoprimes(inpt))