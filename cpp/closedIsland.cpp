#include <vector>
#include <iostream>
#include <array>
using namespace std;


struct pos {
    int r;
    int c;
};

class Solution {
public:
    int closedIsland(vector<vector<int>>& grid) {
        int nclosed = 0;

        for (int i = 1; i < grid.size() - 1; i++) {
            for (int j = 1; j < grid[0].size() - 1; j++) {
                if (grid[i][j] == 0) {
                    nclosed += 1;
                    bfs(pos{i, j}, grid);
                }
            }
        }
        return nclosed;
    }

    vector<pos> neighbors(pos root, vector<vector<int>>& grid) {
        vector<pos> result;

        constexpr array<pos, 4> directions = {{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}};

        for (const auto& dir : directions) {
            int nr = root.r + dir.r;
            int nc = root.c + dir.c;
            if (nr > 0 && nr < grid.size() - 1 && nc > 0 && nc < grid[0].size() - 1 && grid[nr][nc] == 0) {
                result.push_back(pos{nr, nc});
            }
        }
        return result;
    }

    void bfs(pos root, vector<vector<int>>& grid) {
        grid[root.r][root.c] = 1;
        for (pos p: neighbors(root, grid)) {
            bfs(p, grid);
        }
    }
};
