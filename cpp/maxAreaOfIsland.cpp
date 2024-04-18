#include <vector>
#include <queue>
#include <tuple>
#include <set>

using namespace std;


class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = 0;
        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid[0].size(); c++) {
                if (!grid[r][c]) continue;                
                m = max(dfs(make_tuple(r, c), grid), m);
            }
        }
        return m;
    }

    vector<tuple<int, int>> neighbors(int r, int c, vector<vector<int>> grid) {
        vector<tuple<int, int>> p = {make_tuple(r + 1, c), make_tuple(r - 1, c), make_tuple(r, c + 1), make_tuple(r, c - 1)};
        vector<tuple<int, int>> ret;

        for (tuple<int,int> t : p) {
            if (get<0>(t) >= 0 && get<0>(t) < grid.size() && get<1>(t) >= 0 && get<1>(t) < grid[0].size()) {
                ret.push_back(t);
            }
        }
        return ret;   
    }

    int dfs(tuple<int, int> root, vector<vector<int>>& grid) {
        queue<tuple<int, int>> q;
        int total = 0;

        q.push(root);  
        grid[get<0>(root)][get<1>(root)] = 0;

        while (!q.empty()) {
            tuple<int, int> c = q.front();
            q.pop();
            total += 1;

            for (tuple<int, int> t : neighbors(get<0>(c), get<1>(c), grid)) {
                if (!grid[get<0>(t)][get<1>(t)]) continue;
                q.push(t);
                grid[get<0>(t)][get<1>(t)] = 0;
            }
        }
        return total;
    }
};