#include <vector>
using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        int m = 0;
        while (l <= r) {
            m = (l + r) / 2;
            if (nums[m] == target) return m;
            else if (nums[m] < target) l = m + 1;
            else r = m - 1;
        }

        if (l < nums.size() && nums[l] < target) {
            return l + 1;
        }
        return l;
    }
};