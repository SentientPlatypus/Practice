#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;


/*
Example 1:

Input: nums = [4,3,6,16,8,2]
Output: 3
Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.
Example 2:

Input: nums = [2,3,5,6,7]
Output: -1
Explanation: There is no square streak in nums so return -1.
*/


class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        unordered_set<int> visited;
        int res = 0;

        for (int c : nums) {
            if (visited.find(c) != visited.end()) {
                continue;
            }

            int current = c;
            int streak = 1;

            while ((long long)current * current <= 1e5 && binarySearch(nums, current * current)) {
                current *= current;
                visited.insert(current);
                streak++;
            }
            res = max(res, streak);
        }
        return res < 2 ? -1 : res;
    }

    bool binarySearch(vector<int>& nums, long long target) {
        int l = 0;
        int r = nums.size() - 1; 

        while (l <= r) {
            int m = (l + r) / 2;

            if (nums[m] == target) {
                return true;
            }

            if (nums[m] > target) {
                r = m - 1;  
            } else {
                l = m + 1;
            }
        }
        return false;
    }
};
