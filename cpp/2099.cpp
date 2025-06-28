#include <vector>
#include <algorithm>

using namespace std;


class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        vector<int> nums_copy = nums; 
        sort(nums.begin(), nums.end(), greater<int>());
        vector<int> wanted = vector<int>(nums.begin(), nums.begin() + k);
        vector<int> answer;


        for (int i = 0; i < nums.size(); i++) {
            int n = nums_copy[i];
            if (find(wanted.begin(), wanted.end(), n) != wanted.end()) {
                answer.push_back(n);
            }
        }
        return answer;
    }
};