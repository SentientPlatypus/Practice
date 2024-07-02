#include <vector>
#include <unordered_map>
#include <algorithm>



// Example 1:

// Input: nums1 = [1,2,2,1], nums2 = [2,2]
// Output: [2,2]
// Example 2:

// Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
// Output: [4,9]
// Explanation: [9,4] is also accepted.

using namespace std;
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> counts;
        vector<int> result;

        for (int num : nums1) {
            counts[num]++;
        }

        for (int num : nums2) {
            if (counts[num] > 0) {
                result.push_back(num);
                counts[num]--;
            }
        }
        return result;
    }
};
