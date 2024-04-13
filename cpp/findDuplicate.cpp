#include <vector>
using namespace std;

class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int s = 0; int f = 0; int s1 = 0;

        while (1) {
            s = nums[s];
            f = nums[nums[f]];

            if (s == f) break;
        }

        while (1) {
            s = nums[s];
            s1 = nums[s1];

            if (s1 == s) return s;
        }
        return -1;
    }
};