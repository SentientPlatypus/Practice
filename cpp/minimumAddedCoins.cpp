#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minimumAddedCoins(vector<int>& coins, int target) {
        //[1,4,10,5,7,19], target = 19. X is obtainable if there is a subsequence of coins that adds to target.
        sort(coins.begin(), coins.end());
        
        int m = 1;
        int added = 0;
        int i = 0;

        while (m <= target) {
            if (i < coins.size() && coins[i] <= m) m += coins[i ++];
            else {
                m += m;
                added ++;
            }
        }
        return added;
    }
};