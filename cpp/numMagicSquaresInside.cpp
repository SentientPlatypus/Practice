#include <vector>
#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int rbound = grid.size();
        int cbound = grid[0].size();
        int count = 0;

        for (int row = 0; row <= rbound - 3; ++row) {
            for (int col = 0; col <= cbound - 3; ++col) {
                if (isMagicSquare(row, col, grid)) {
                    count++;
                }
            }
        }

        return count;
    }

    bool isMagicSquare(int r, int c, const vector<vector<int>>& grid) {
        vector<int> square(9);
        int index = 0;

        // Extract the 3x3 square
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                square[index++] = grid[r + i][c + j];
            }
        }

        // Check for magic square
        int sum = square[0] + square[1] + square[2];
        if (sum != square[3] + square[4] + square[5] || 
            sum != square[6] + square[7] + square[8]) {
            return false;
        }

        if (square[0] + square[3] + square[6] != sum || 
            square[1] + square[4] + square[7] != sum || 
            square[2] + square[5] + square[8] != sum) {
            return false;
        }

        if (square[0] + square[4] + square[8] != sum || 
            square[2] + square[4] + square[6] != sum) {
            return false;
        }

        // Check for distinct values from 1 to 9
        unordered_set<int> unique_values(square.begin(), square.end());
        if (unique_values.size() != 9) {
            return false;
        }

        for (int i = 1; i <= 9; ++i) {
            if (unique_values.find(i) == unique_values.end()) {
                return false;
            }
        }

        return true;
    }
};