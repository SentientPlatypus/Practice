#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

class Solution {
public: 

    bool canPlace(int x, vector<int> &position, int m) {
        int prevBallPos = position[0];
        int ballsPlaced = 1;

        for (int i = 1; i < position.size() && ballsPlaced < m; ++i) {
            int currPos = position[i];
            if (currPos - prevBallPos >= x) {
                ballsPlaced += 1;
                prevBallPos = currPos;
            }
        }
        return ballsPlaced == m;
    }

    int maxDistance(vector<int>& position, int m) {
        int r = 0;
        int n = position.size();
        sort(position.begin(), position.end());

        int l = 1;
        int h = ceil(position[n - 1] / (m - 1.0));
        while (l <= h) {
            int mid = l + (h - l) / 2;
            if (canPlace(mid, position, m)) {
                r = mid;
                l = mid + 1;
            } else {
                h = mid - 1;
            }
        }
        return r;
    }
};