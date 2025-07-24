#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_set<int> seen;
        int res = 0;
        int cur = 0;
        int l = 0;


        for (int r = 0; r < nums.size(); r++) {
            if (seen.find(nums[r]) != seen.end()) {
                while (nums[l] != nums[r]) {
                    seen.erase(nums[l]);
                    cur -= nums[l];
                    l++;
                }
                cur -= nums[l];
                l++;
            }
            cur += nums[r];
            seen.insert(nums[r]);
            res = max(cur, res);
        }
        return res;
    }
};