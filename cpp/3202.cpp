class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        vector<vector<int>> dp(k, vector<int>(k, 0));

        int ans = 0;

        for (int num : nums) {
            num %= k;

            for (int prev = 0; prev < k; prev++) {
                dp[prev][num] = dp[num][prev] + 1;
                ans = max(ans, dp[prev][num]);
            }
        }
        return ans;
    }
};