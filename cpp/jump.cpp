#include <vector>
#include <unordered_map>
#include <queue>
#include <unordered_set>



using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        unordered_map<int, vector<int>> tree;
        unordered_map<int, int> distances;
        unordered_set<int> visited;

        for (int i = 0; i < nums.size(); i++) {
            int maxjumps = nums[i];
            for (int j = 1; j <= maxjumps; j++) tree[i].push_back(i + j);
        }

        //Tree is created.
        //now lets do bfs
        queue<int> q;
        q.push(0);
        distances[0] = 0;
        visited.insert(0);

        while (!q.empty()) {
            int cur = q.front();
            q.pop();

            for (int child : tree[cur]) {
                if (visited.find(child) == visited.end()) {
                    visited.insert(child);
                    distances[child] = distances[cur] + 1;
                    q.push(child);
                }
            }
        }

        return distances[nums.size() - 1];
    }
};