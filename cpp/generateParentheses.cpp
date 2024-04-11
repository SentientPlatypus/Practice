#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {

        if (n == 1) return {"()"};

        vector<vector<string>> dp(n + 1);
        dp[0] = {""};
        dp[1] = {"()"};

        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                for (string x : dp[j]) {
                    for (string y : dp[i - j - 1]) {
                        dp[i].push_back("(" + x + ")" + y);
                    }
                }
            }
        }

        return dp[n];
    }
};