#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        vector<int> sums;

        for (int i = 0; i < nums.size(); i++) {
            int sum = 0;
            for (int j  = i; j < nums.size(); j++) {
                sum += nums[j];
                sums.push_back(sum);
            }
        }

        sort(sums.begin(), sums.end());
        int rangeSum = 0;
        int mod = 1e9 + 7;
        for (int i = left - 1; i <= right - 1; i++) {
            rangeSum = (rangeSum + sums[i]) % mod;
        }   
        return rangeSum;
    }
};