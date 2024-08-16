#include <vector>
#include <queue>
#include <algorithm>
using namespace std;


//[[1,2,3],[4,5],[1,2,3]]
class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int s = arrays[0][0];
        int b = arrays[0].back();

        int max_d = 0;

        for (int i = 1; i < arrays.size(); i++) {
            max_d = max(max_d, abs(s - arrays[i].back()));
            max_d = max(max_d, abs(b - arrays[i][0]));
            s = min(s, arrays[i][0]);
            b = max(b, arrays[i].back());
        }

        return max_d;
    }
};