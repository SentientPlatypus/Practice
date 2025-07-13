    #include <vector>
    #include <algorithm>

    using namespace std;


    class Solution {
    public:
        vector<int> maxSubsequence(vector<int>& nums, int k) {
            vector<pair<int, int>> num_idx;
            for (int i = 0; i < nums.size(); ++i) {
                num_idx.push_back({nums[i], i});
            }

            // Sort by value descending
            sort(num_idx.begin(), num_idx.end(), [](const pair<int,int>& a, const pair<int,int>& b) {
                return a.first > b.first;
            });

            vector<pair<int, int>> topk(num_idx.begin(), num_idx.begin() + k);

            sort(topk.begin(), topk.end(), [](const pair<int,int>& a, const pair<int,int>& b) {
                return a.second < b.second;
            });

            vector<int> answer;
            for (auto& p : topk) answer.push_back(p.first);
            return answer;
        }
    };