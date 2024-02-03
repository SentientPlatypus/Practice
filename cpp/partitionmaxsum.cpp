#include <vector>
#include <algorithm>

using namespace std;
class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        vector<int> dp(arr.size()+1, 0);
        
        for (int i = 0; i <= arr.size(); i++) {
            int curSum = 0, curMax = 0;

            for (int j = 1; j <= k && i - j >=0; j++) {
                curMax = max(curMax, arr[i - j]);
                curSum = max(curSum, dp[i - j] + curMax * j);
            }
            dp[i] = curSum;
        }
        return dp[arr.size()];
    }
};