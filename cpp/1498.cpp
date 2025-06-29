#include <vector>
#include <algorithm>

using namespace std;


class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int left = 0, right = n - 1;
        int mod = 1e9 + 7;
        int count = 0;
        vector<int> power(n, 1);
        for (int i = 1; i < n; ++i) {
            power[i] = (power[i - 1] * 2) % mod;
        }
        while (left <= right) {
            if (nums[left] + nums[right] <= target) {
                count = (count + power[right - left]) % mod;
                left++;
            } else {
                right--;
            }
        }
        return count;
    }
};