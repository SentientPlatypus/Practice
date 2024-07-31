#include <vector>

using namespace std;

class Solution {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        int n = books.size();
        vector<int>dp(n + 1, __INT_MAX__);
        dp[0] = 0;

        for (int i = 0; i < n + 1; i++) {
            int totalw = 0;
            int maxh = 0;
            for (int j = i - 1; j > 0; j--) {
                totalw += books[j - 1][0];
                if (totalw > shelfWidth) break;
                maxh = max(maxh, books[j - 1][1]);
                dp[i] = min(dp[i], dp[j - 1] + maxh);
            }
        }
        return dp[n];
    }
};