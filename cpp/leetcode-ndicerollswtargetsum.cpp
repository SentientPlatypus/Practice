#include <vector>

using namespace std;

class Solution {
public:
    const int m = 1000000007;
    int numRollsToTarget(int n, int k, int target) {
        vector<vector<int>> dp(n + 1, vector<int>(target + 1, -1));
        return recursion(dp, n, k, target);
    }

    int recursion(std::vector<std::vector<int>>& dp, int n, int k, int target) {
        if (target == 0 && n == 0) {
            return 1;
        }

        if (n == 0 || target <= 0) {
            return 0;
        }

        if (dp[n][target] != -1) {
            return dp[n][target] % m;
        }

        int ways = 0;
        for (int i = 1; i <= k; ++i) {
            ways = (ways + recursion(dp, n - 1, k, target - i) % m) % m;
        }

        dp[n][target] = ways;
        return dp[n][target];
    }
};