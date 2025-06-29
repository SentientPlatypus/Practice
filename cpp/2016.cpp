#include <vector>
using namespace std;


class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int ans = -1;
        int n = nums.size();
        int min = nums[0];

        for (int i = 1; i < n; i++) {
            if (nums[i] <= min) {
                min = nums[i];
            } else {
                ans = max(ans, nums[i] - min);
            }
        }

        return ans;
    }
};