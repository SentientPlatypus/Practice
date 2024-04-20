#include <vector>
#include <queue>
#include <utility>


using namespace std;


struct pos {
    int r;
    int c;
};


class Solution {
public:
    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        vector<vector<int>> ret;
        for (int i = 0; i < land.size(); i ++) {
            for (int j = 0; j < land[0].size(); j++) {
                if (land[i][j]) {
                    ret.push_back(bfs(i, j, land));
                }
            }
        }
        return ret;
    }

    vector<pos> neighbors(pos node, vector<vector<int>>&grid) {
        vector<pos> result;
        static const vector<pos> offsets = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (const auto& offset : offsets) {
            int nr = node.r + offset.r;
            int nc = node.c + offset.c;
            if (nr >= 0 && nr < grid.size() && nc >= 0 && nc < grid[0].size() && grid[nr][nc]) {
                result.push_back({nr, nc});
            }
        }
        return result;
    }

    vector<int> bfs(int r, int c, vector<vector<int>>&grid) {
        queue<pos> q;
        vector<int> ret;


        q.push(pos{r, c});
        grid[r][c] = 0;

        pos br = pos{r, c};
        pos tl = pos{r, c};
        while (!q.empty()) {
            pos cur = q.front();
            q.pop();

            for (pos p :neighbors(cur, grid)) {
                grid[p.r][p.c] = 0;
                q.push(p);
                tl.r = min(tl.r, p.r);
                tl.c = min(tl.c, p.c);
                br.r = max(br.r, p.r);
                br.c = max(br.c, p.c);
            }
        }
        ret.push_back(tl.r);
        ret.push_back(tl.c);
        ret.push_back(br.r);
        ret.push_back(br.c);
        return ret;
    }
};