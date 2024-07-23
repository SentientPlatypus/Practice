#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        unordered_map<int, int> mp;
        for (int i : nums) mp[i] += 1;


        int i, j, key, keyFreq;
        for (i = 1; i < nums.size(); i++) {
            key = nums[i];
            keyFreq = mp[key];

            j = i - 1;

            while (j >= 0 && (mp[nums[j]] > keyFreq || (mp[nums[j]] == keyFreq && nums[j] < key))) {
                nums[j + 1] = nums[j];
                j--;
            }
            nums[j + 1] = key;
        }

        return nums;
    }
};