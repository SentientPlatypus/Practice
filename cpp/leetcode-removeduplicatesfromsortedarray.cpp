
#include<vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int i = 1;
        while (i < nums.size()) {
            if (nums[i] == nums[i - 1]) {
                nums.erase(nums.begin() + i);
                i -= 1;
            }
            i += 1;
        }
        
        return nums.size();
    }
};