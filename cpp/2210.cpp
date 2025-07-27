#include <vector>
using namespace std;

class Solution {
public:
    int countHillValley(vector<int>& nums) {
        int res = 0;
        int prevDir; // 0: not initialized, 1: down, 2: up

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i-1]) {
                continue;
            }

            int curDir = (nums[i] > nums[i - 1]) ? 2 : 1;
            if (!prevDir) res--;
            if (prevDir != curDir) res++;
            prevDir = curDir;
        }
        return res;
    }
};