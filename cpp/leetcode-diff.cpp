class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& grid) {
        vector<vector<int>> diff(grid.size(), vector<int>(grid[0].size(), 0));
        vector<int> onesRow(grid.size(), 0);
        vector<int> onesCol(grid[0].size(), 0);
        vector<int> zerosRow(grid.size(), 0);
        vector<int> zerosCol(grid[0].size(), 0);

        for(int r = 0; r < grid.size(); r ++) {
            vector<int> row;
            for (int c = 0; c < grid[0].size(); c ++) {
                if (grid[r][c] == 1) {
                    onesRow[r] += 1;
                    onesCol[c] += 1;
                }
                if (grid[r][c] == 0) {
                    zerosRow[r] += 1;
                    zerosCol[c] += 1;
                }
            }
        }



        for (int r = 0; r < grid.size(); r ++) {
            for (int c = 0; c < grid[0].size(); c ++) {
                diff[r][c] = onesRow[r] + onesCol[c] - zerosRow[r] - zerosCol[c];
            }
        }
        return diff;
    }
};