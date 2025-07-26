#include <vector>
#include <unordered_set>
#include <algorithm>
#include <numeric>
using namespace std;


class Solution {
public:
    int maxSum(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        unordered_set<int> seen;
        int maxN = nums[0];

        for (int n : nums) {
            maxN = max(maxN, n);
            if (n > 0) {
                seen.insert(n);
            }
        }
        seen.insert(maxN);
        return accumulate(seen.begin(), seen.end(), 0);
    }
};