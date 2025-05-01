#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> getRow(int rowIndex) {
            if (rowIndex == 0) {
                return {1};
            }
            if (rowIndex == 1) {
                return {1, 1};
            }

            vector<int> row(rowIndex + 1, 0);
            row[0] = 1;

            vector<int> prevRow = getRow(rowIndex - 1);
            for (int i = 1; i < rowIndex; ++i) {
                row[i] = prevRow[i - 1] + prevRow[i];
            }
            row[rowIndex] = 1;
            return row;

        }
    };