#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;


class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        vector<int> ans;
        unordered_set<int> seen;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if (nums[i] == key) {
                for (int j = max(0, i - k); j <= min(n - 1, i + k); j++) {
                    seen.insert(j);
                }
            }
        }
        ans.assign(seen.begin(), seen.end());
        sort(ans.begin(), ans.end());
        return ans;
    }
};