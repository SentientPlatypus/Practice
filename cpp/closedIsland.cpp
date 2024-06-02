#include <vector>
#include <iostream>
#include <array>
#include <queue>
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
                    if (bfs(pos{i, j}, grid)) {
                        nclosed++;
                    }
                }
            }
        }
        return nclosed;
    }

    bool bfs(pos root, vector<vector<int>>& grid) {
        bool isClosed = true;
        vector<pos> queue = {root};

        grid[root.r][root.c] = 1;

        constexpr array<pos, 4> directions = {{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}};

        while (!queue.empty()) {
            pos current = queue.front();
            queue.erase(queue.begin());

            for (const auto& dir : directions) {
                int nr = current.r + dir.r;
                int nc = current.c + dir.c;

                if (nr >= 0 && nr < grid.size() && nc >= 0 && nc < grid[0].size() && grid[nr][nc] == 0) {
                    grid[nr][nc] = 1;
                    queue.push_back({nr, nc});
                } else if (nr < 0 || nr >= grid.size() || nc < 0 || nc >= grid[0].size()) {
                    isClosed = false;
                }
            }
        }
        return isClosed;
    }
};
