class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp = [-99999 for n in arr] #let dp[i] represent the maximum subarray sum that ends at i.
        dp_delete = [-9999 for n in arr] #max sub array ending at i with one deletion


        dp[0] = arr[0]
        dp_delete[0] = arr[0]

        res = dp[0]
        for i in range(1, len(arr)):
            dp[i] = max(dp[i - 1] + arr[i], arr[i])


            dp_delete[i] = max(dp[i - 1], dp_delete[i - 1] + arr[i])

            res = max(dp_delete[i], dp[i], res)

        return res

