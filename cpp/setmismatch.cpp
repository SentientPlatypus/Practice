#include <numeric>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int> r(2, 0);
        vector<int> n(nums.size() + 1, 0);
        
        for (int i = 1; i <= nums.size(); i ++) {
            n[nums[i - 1]] ++;
        }

        for (int i = 0; i < n.size(); i ++) {
            if (n[i] == 2) {
                r[0] = i;
            }
            if (n[i] == 0) {
                r[1] = i;
            }
        }
        return r;

    }
};