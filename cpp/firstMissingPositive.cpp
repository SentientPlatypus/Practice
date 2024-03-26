#include <unordered_map>
#include <limits.h>
#include <algorithm>
#include <vector>
class Solution {
public:
    int firstMissingPositive(std::vector<int>& nums) {
        std::unordered_map<int, bool> umap;

        int m = nums[0];
        for (int k : nums) {
            umap[k] = true;
            m= std::max(k, m);
        }

        if (m == INT_MAX) {
            m -= 1;
        } 

        for (int i = 1; i <= m + 1; i ++) {
            if (umap.find(i) == umap.end()) {
                return i;
            }
        }
        return 1;
    }
};