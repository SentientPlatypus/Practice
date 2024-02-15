#include <algorithm>
#include <vector>
using namespace std;
class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        sort(nums.rbegin(), nums.rend()); 
        

        int start = 0;
        while (start < nums.size()) {
            long sum = 0;
            for (int i = start + 1; i < nums.size(); i++) {
                sum += nums[i]; 
            }
            if (sum <= nums[start]) {
                start += 1;
                continue;
            }
            else{
                return sum + nums[start];
            }
        }
        return -1;
    }
};