#include <vector>

using namespace std;


class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int totalOnes = 0;
        int n = nums.size();
        
        for (int i : nums) totalOnes += i == 1;

        vector<int> extendedNums = nums;
        extendedNums.insert(extendedNums.end(), nums.begin(), nums.end());

        int l = 0;
        int r = totalOnes - 1;
        int minSwaps = __INT_MAX__;
        int swaps = 0;

        for (int i = l; i <= r; i++) if (extendedNums[i] == 0) swaps++;
            
        
        minSwaps = min(minSwaps, swaps);


        while (r < extendedNums.size() - 1) {
            if (extendedNums[l] == 0) swaps--;
            l++;
            r++;
            if (extendedNums[r] == 0) swaps++;
            minSwaps = min(minSwaps, swaps);
        }

        return minSwaps;
    }
};