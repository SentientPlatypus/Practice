#include <vector>
#include <queue>
#include <utility>
#include <array>



using namespace std;
struct pos {
    int r;
    int c;
};



class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        for (int i = 0; i < grid.size(); i ++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    count += 1;
                    dfs(pos{i, j}, grid);
                }
            }
        }
        return count;
    }

    vector<pos> neighbors(pos root, const vector<vector<char>>& grid) {
        vector<pos> result;
        const int rows = grid.size();
        const int cols = grid[0].size();

        // Define possible directions (up, down, left, right)
        constexpr array<pos, 4> directions = {{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}};

        // Iterate over directions and check for valid neighbors
        for (const auto& dir : directions) {
            int nr = root.r + dir.r;
            int nc = root.c + dir.c;
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '1') {
                result.push_back({nr, nc});
            }
        }
        return result;
    }


    void dfs(pos root, vector<vector<char>>& grid) {
        queue<pos> q;
        q.push(root);
        grid[root.r][root.c] = 0;

        while (!q.empty()) {
            pos c = q.front();
            q.pop();

            for (pos p : neighbors(c, grid)) {
                grid[p.r][p.c] = '0';
                q.push(p);
            }
        }
    }
};