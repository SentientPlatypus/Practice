#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        vector<int> xs;
        for (vector<int> p:points) {
            xs.push_back(p[0]);
        }

        sort(xs.begin(), xs.end());

        int maxgap = -1000;
        for (int i = 0; i < xs.size() - 1; i ++) {
            maxgap = max(xs[i + 1] - xs[i], maxgap);
        }

        return maxgap;
    }
};