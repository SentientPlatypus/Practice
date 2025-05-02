#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    public:
        int maxProfit(vector<int>& prices) {
            int maxProfit = 0;
            int minPrice = prices[0];

            for (int i = 0; i < prices.size(); i++) {
                maxProfit = max(maxProfit, prices[i] - minPrice);

                minPrice = min(minPrice, prices[i]);
            }

            return maxProfit;
        }
    };