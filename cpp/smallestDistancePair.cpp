#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        auto countPairs = [&](int mid) {
            int count = 0;
            int left = 0;
            for (int right = 0; right < n; ++right) {
                while (nums[right] - nums[left] > mid) {
                    ++left;
                }
                count += right - left;
            }
            return count;
        };

        int low = 0;
        int high = nums[n - 1] - nums[0];
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (countPairs(mid) < k) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        
        return low;
    }
};