#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findLHS(vector<int>& nums) {
        int ans = 0;
        sort(nums.begin(), nums.end());
        int l = 0, r = 0;
        while (r < nums.size()) {
            if (nums[r] - nums[l] == 1) {
                ans = max(ans, r - l + 1);
                r++;
            } else if (nums[r] - nums[l] > 1) {
                l++;
            } else {
                r++;
            }
        }
        return ans;
    }
};