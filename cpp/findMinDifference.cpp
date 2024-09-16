#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        int mindiff = __INT_MAX__;

        vector<int> minutes(timePoints.size());

        for (int i = 0; i < timePoints.size(); ++i) {
            int h = stoi(timePoints[i].substr(0, 2));
            int m = stoi(timePoints[i].substr(3));
            minutes[i] = h * 60 + m;
        }

        sort(minutes.begin(), minutes.end());

        for (int i = 1; i < timePoints.size(); i++) {
            mindiff = min(mindiff, minutes[i] - minutes[i - 1]);
        }

        mindiff = min(mindiff, 24 * 60 - minutes.back() + minutes.front());

        return mindiff;
    }
};