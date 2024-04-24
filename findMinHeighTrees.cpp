#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) return {0}; // Special case: only one node

        vector<vector<int>> adj(n);
        vector<int> neighb(n, 0);

        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
            neighb[u]++;
            neighb[v]++;
        }

        queue<int> leaves;
        // Step 2: Enqueue leaf nodes
        for (int i = 0; i < n; ++i) {
            if (neighb[i] == 1) {
                leaves.push(i);
            }
        }

        while (n > 2) {
            int num_leaves = leaves.size();
            n -= num_leaves;

            for (int i = 0; i < num_leaves; ++i) {
                int leaf = leaves.front();
                leaves.pop();

                for (int neighbor : adj[leaf]) {
                    neighb[neighbor]--;
                    if (neighb[neighbor] == 1) {
                        leaves.push(neighbor);
                    }
                }
            }
        }

        vector<int> res;
        while (!leaves.empty()) {
            res.push_back(leaves.front());
            leaves.pop();
        }

        return res;
    }
};
