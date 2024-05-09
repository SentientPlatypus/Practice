#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>

using namespace std;


class Solution {
public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        vector<vector<int>> dp(n, vector<int>(n, 0));
        vector<int> r(n, 0);
        unordered_map<int, vector<int>> tree;

        for (vector<int> v : edges) {
            tree[v[0]].push_back(v[1]);
            
        }

        bfs0(0, tree, dp); //Initializes distances to root node. (eg. depths as well!)
        bfs(0, n, tree, dp);

        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int k = 0; k < n; k++) {
                cout << dp[i][k];
                sum += dp[i][k];
            }
            cout << endl;
            r[i] = sum;
        }
        return r;
    }

    void bfs0(int start, unordered_map<int, vector<int>>& t, vector<vector<int>>& dp) {
        queue<int> q;

        q.push(start);
        dp[start][start] = 0;

        while (!q.empty()) {
            int parent = q.front();
            q.pop();
            for (int child : t[parent]) {
                dp[start][child] = dp[start][parent] + 1;
                q.push(child);
            }
        }
    }

    void bfs(int start, int n, unordered_map<int, vector<int>>& t, vector<vector<int>>& dp) {
        unordered_set<int> v;
        queue<int> q;
        q.push(start);
        v.insert(start);

        while (!q.empty()) {
            int parent = q.front();
            cout << parent << " ";
            q.pop();
            for (int child : t[parent]) {
                cout << child;
                for (int i = 0; i < n; i++) {
                    if (child == i) dp[child][i] = 0;
                    else dp[child][i] = abs(dp[parent][i] + (v.find(child) != v.end() ? 1 : - 1));
                }
                v.insert(child);
                q.push(child);
            }
            cout << endl;
        }
    }
};