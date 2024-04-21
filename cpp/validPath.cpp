#include <vector>
#include <map>
#include <queue>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        map<int, vector<int>> mp;
        unordered_set<int> v;
        

        for (vector<int> v :edges) {
            mp[v[0]].push_back(v[1]);
            mp[v[1]].push_back(v[0]);
        }

        queue<int> q;
        q.push(source);
        v.insert(source);

        while (!q.empty()) {
            int c = q.front();
            q.pop();
            if (c == destination) return true;

            for (int k : mp[c]) {
                if (v.find(k) == v.end()) {
                    v.insert(k);
                    q.push(k);
                }
            }
        }
        return false;
    }
};