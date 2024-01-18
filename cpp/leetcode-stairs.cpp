#include <vector>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 3) return n;
        vector<int> dp(n + 1, 0);
        return fib(n, dp);
    }

    int fib(int n, vector<int>& dp) {
        if (n <= 3) return n;
        if (dp[n]) return dp[n];
        dp[n] = fib(n - 1, dp) + fib(n - 2, dp);
        return dp[n];
    }
};