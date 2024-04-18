#include <vector>
#include <queue>
#include <set>
#include <tuple>

using namespace std;

class Solution {
public:
    vector<tuple<int, int>> neighbors(int r, int c, vector<vector<int>>& grid) {
        vector<tuple<int, int>> p = {make_tuple(r + 1, c), make_tuple(r - 1, c), make_tuple(r, c + 1), make_tuple(r, c - 1)};
        vector<tuple<int, int>> ret;

        for (tuple<int,int> t : p) {
            if (get<0>(t) >= 0 && get<0>(t) < grid.size() && get<1>(t) >= 0 && get<1>(t) < grid[0].size()) {
                ret.push_back(t);
            }
        }
        return ret;   
    }

    int islandPerimeter(vector<vector<int>>& grid) {
        tuple<int, int> start;
        bool found = false;
        for (int r = 0; r < grid.size(); r++) {
            for (int c = 0; c < grid[0].size(); c++) {
                if (grid[r][c]) {
                    start = make_tuple(r, c);
                    found = true;
                    break;
                }
            }
            if (found) break;
        }

        set<tuple<int, int>> s;
        queue<tuple<int, int>> q;
        int t = 0;

        s.insert(start);
        q.push(start);

        while (!q.empty()) {
            tuple<int, int> c = q.front();
            q.pop();

            int p = 4;
            for (tuple<int, int> tu : neighbors(get<0>(c), get<1>(c), grid)) {
                if (!grid[get<0>(tu)][get<1>(tu)]) continue;
                p -= 1;
                if (s.find(tu) == s.end()) {
                    q.push(tu);
                    s.insert(tu);
                }
            }
            t += p;
        }
        return t;
    }
};