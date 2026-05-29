class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> curComb;

        auto backtrack = [&](auto& self, int start, int sum) -> void {
            if (sum == target) {
                res.push_back(curComb);
                return;
            }
            if (sum > target) {
                return;
            }
            
            for (int i = start; i < candidates.size(); i++) {
                if (i > start && candidates[i] == candidates[i - 1]) {
                    continue;
                }

                curComb.push_back(candidates[i]);
                self(self, i + 1, sum + candidates[i]);
                curComb.pop_back();
            }
        };

        backtrack(backtrack, 0, 0);
        return res;
    }
};
