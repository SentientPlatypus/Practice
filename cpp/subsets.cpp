#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> op;
        solve(nums, 0, op, res);
        return res;
    }
    
    void solve(vector<int>& nums, int start, vector<int>& op, vector<vector<int>>& res) {
        if (nums.size() == start) {
            res.push_back(op);
            return;
        }
        
        solve(nums, start + 1, op, res);
        op.push_back(nums[start]);
        solve(nums, start + 1, op, res);
        op.pop_back();
    }
};