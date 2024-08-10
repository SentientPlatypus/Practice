#include <vector>
#include <string>
#include <queue>

using namespace std;


class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        int gridSize = grid.size();
        vector<vector<int>> expandedGrid(gridSize * 3, vector<int>(gridSize * 3, 0));


        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                int baseRow = i * 3;
                int baseCol = j * 3;
                if (grid[i][j] == '\\') {
                    expandedGrid[baseRow][baseCol] = 1;
                    expandedGrid[baseRow + 1][baseCol + 1] = 1;
                    expandedGrid[baseRow + 2][baseCol + 2] = 1;
                } else if (grid[i][j] == '/') {
                    expandedGrid[baseRow][baseCol + 2] = 1;
                    expandedGrid[baseRow + 1][baseCol + 1] = 1;
                    expandedGrid[baseRow + 2][baseCol] = 1;
                }
            }
        }

        int regionCount = 0;
        for (int i = 0; i < gridSize * 3; i++) {
            for (int j = 0; j < gridSize * 3; j++) {
                if (expandedGrid[i][j] == 0) {
                    floodFill(expandedGrid, i, j);
                    regionCount++;
                }
            }
        }
        return regionCount;
    }
    vector<pair<int,int>> neighbors(const vector<vector<int>>& expandedGrid, int row, int col) {
        vector<pair<int, int>> neighb = {{row, col + 1}, {row, col - 1}, {row + 1, col}, {row - 1, col}};
        vector<pair<int,int>> res;
        int n = expandedGrid.size();
        for (pair p : neighb) {
            int r = p.first;
            int c = p.second;
            if (r >= 0 && c >= 0 && r < n && c < n && expandedGrid[r][c] == 0) res.push_back(p);
        }
        return res;
    }

    void floodFill(vector<vector<int>>& expandedGrid, int row, int col) {
        queue<pair<int, int>> q;

        expandedGrid[row][col] = 1;

        q.push({row, col});

        while (!q.empty()) {
            pair<int, int> c = q.front();
            q.pop();

            for (pair p : neighbors(expandedGrid, c.first, c.second)) {
                expandedGrid[p.first][p.second] = 1;
                q.push(p);
            }
        }
    }
};